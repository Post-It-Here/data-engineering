from typing import List
from pydantic import BaseModel


class PredictionBase(BaseModel):
    prediction: str


class PredictionCreate(PredictionBase):
    pass


class Prediction(PredictionBase):
    id: int
    user_input: int

    class Config:
        orm_mode = True


class UserInputBase(BaseModel):
    title: str
    description: str = None


class UserInputCreate(UserInputBase):
    pass

class UserInput(UserInputBase):
    id: int
    predictions: List[Prediction] = []

    class Config:
        orm_mode = True