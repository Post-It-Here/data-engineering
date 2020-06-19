from fastapi import APIRouter
from pydantic import BaseModel


class UserRequest(BaseModel):
    title: str
    description: str


class Prediction(UserRequest):
    subreddit: str


api_routes = APIRouter()


@api_routes.post("/predict", response_model=Prediction)
async def predict_sub(user_request: UserRequest):
    title = user_request.title
    description = user_request.description
    # TODO
    # Do Stuff
    prediction = {
        "title": title,
        "description": description,
        "subreddit": "r/wallstreetbets",
    }

    return prediction
