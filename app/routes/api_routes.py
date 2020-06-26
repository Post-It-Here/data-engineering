from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ValidationError, validator
from typing import List
from ..services.data_model import post_predictions

from ..core import schema, database_models, crud
from ..core.database import SessionLocal, engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    database_models.Base.metadata.drop_all(bind=engine)
    database_models.Base.metadata.create_all(bind=engine)


class UserRequest(BaseModel):
    title: str
    description: str

    class Config:
        schema_extra = {
            "example": {"title": "Is data science cool?", "description": "Yeah it is."}
        }


class PredictionOne(BaseModel):
    subreddit: str


class UserRequestMany(UserRequest):
    number: int = 3

    class Config:
        schema_extra = {
            "example": {
                "title": "Is data science cool?",
                "description": "Yeah it is.",
                "number": 3,
            }
        }


class PredictionMany(BaseModel):
    subreddits: List[str]


api_routes = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_predictions_db(db, user_request: schema.UserInputBase, number: int = 1):
    user_input = crud.get_user_input_by_data(
        db, user_request.title, user_request.description
    ) or crud.create_user_input(db, user_request)

    if len(user_input.predictions) < number:
        predictions = get_predictions_model(user_input, number)

        for prediction in predictions:
            crud.create_prediction(db, prediction, input_id=user_input.id)
        db.refresh(user_input)
    else:
        predictions = [prediction.subreddit for prediction in user_input.predictions]
    return predictions[:number]


def get_predictions_model(user_input: schema.UserInput, number=1):

    post = f"{user_input.title} {user_input.description}"

    predictions = [f"r/{x}" for x in post_predictions(post, number).index.tolist()]

    prediction = {"subreddits": predictions}
    return predictions


@api_routes.post("/predict_many", response_model=PredictionMany)
def predict_many(user_request: UserRequestMany, db: Session = Depends(get_db)):
    """Takes a user request and returns a list of compatible subreddits"""

    preds = get_predictions_db(db, user_request, user_request.number)
    return {"subreddits": preds}


@api_routes.post("/predict", response_model=PredictionOne)
def predict_sub(user_request: UserRequest, db: Session = Depends(get_db)):
    """Takes a user request and returns the most compatible subreddit"""

    preds = get_predictions_db(db, user_request)
    prediction = {
        "subreddit": preds[0],
    }

    return prediction
