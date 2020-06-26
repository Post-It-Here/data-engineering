from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ValidationError, validator
from typing import List
from ..services.data_model import post_predictions

from ..core import schema, database_models, crud
from ..core.database import SessionLocal, engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    breakpoint()
    database_models.Base.metadata.create_all(bind=engine)


class UserRequest(BaseModel):
    title: str
    description: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Is data science cool?",
                "description": "Yeah it is."
            }
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
                "number": 3
            }
        }

class PredictionMany(BaseModel):
    subreddits: List[str]


api_routes = APIRouter()


@api_routes.post("/predict_many", response_model=PredictionMany)
def predict_many(user_request: UserRequestMany):
    """Takes a user request and returns a list of compatible subreddits"""

    title = user_request.title
    description = user_request.description
    number = user_request.number
    # TODO
    # Do Stuff

    post = f"{title} {description}"

    predictions = [f"r/{x}" for x in post_predictions(post, number).index.tolist()]

    prediction = {"subreddits": predictions}
    return prediction


@api_routes.post("/predict", response_model=PredictionOne)
def predict_sub(user_request: UserRequest):
    """Takes a user request and returns the most compatible subreddit"""

    title = user_request.title
    description = user_request.description

    post = f"{title} {description}"

    prediction = post_predictions(post, 1).index.tolist()[0]

    prediction = {
        "subreddit": f"r/{prediction}",
    }

    return prediction
