from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from ..services.data_model import post_predictions


class UserRequest(BaseModel):
    title: str
    description: str


class PredictionOne(UserRequest):
    subreddit: str


class PredictionMany(UserRequest):
    subreddit: List[List[str]]


api_routes = APIRouter()


@api_routes.post("/predict", response_model=PredictionOne)
def predict_sub(user_request: UserRequest):
    title = user_request.title
    description = user_request.description
    # TODO
    # Do Stuff

    post = f"{title} {description}"

    prediction = post_predictions(post).index


    prediction = {
        "title": title,
        "description": description,
        "subreddit": f"r/{prediction[0]}",
    }



    return prediction
