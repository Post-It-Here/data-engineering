from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from ..services.data_model import post_predictions


class UserRequest(BaseModel):
    title: str
    description: str


class PredictionOne(BaseModel):
    subreddit: str


class UserRequestMany(UserRequest):
    number: int = 3


class PredictionMany(BaseModel):
    subreddits: List[str]


api_routes = APIRouter()


@api_routes.post("/predict_many", response_model=PredictionMany)
def predict_many(user_request: UserRequestMany):
    title = user_request.title
    description = user_request.description
    number = user_request.number
    # TODO
    # Do Stuff

    post = f"{title} {description}"

    predictions = [f"r/{x}" for x in post_predictions(post, number).index.tolist()]

    prediction = {"title": title, "description": description, "subreddits": predictions}
    return prediction


@api_routes.post("/predict", response_model=PredictionOne)
def predict_sub(user_request: UserRequest):
    title = user_request.title
    description = user_request.description
    # TODO
    # Do Stuff

    post = f"{title} {description}"

    prediction = post_predictions(post, 1).index.tolist()[0]

    prediction = {
        "title": title,
        "description": description,
        "subreddit": f"r/{prediction}",
    }

    return prediction
