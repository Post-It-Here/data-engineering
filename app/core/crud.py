from sqlalchemy.orm import Session

from . import database_models as models
from . import schema

def get_user_input(db:Session, input_id:int):
    return db.query(models.UserInput).filter(models.UserInput.id == input_id).first()


def get_user_input_by_data(db:Session, title=str, description:str=""):
    query = db.query(models.UserInput)\
        .filter(models.UserInput.title == title)\
        .filter(models.UserInput.description)\
        .first()

    return query

def create_user_input(db:Session, user_input: schema.UserInputCreate):
    db_user_input = models.UserInput(
        title = user_input.title,
        description=user_input.description)
    db.add(db_user_input)
    db.commit()
    db.refresh(db_user_input)
    return db_user_input


def create_prediction(db:Session, prediction: schema.PredictionCreate, input_id:int = None):
    db_prediction = models.Prediction(**prediction.dict(), user_input=input_id)
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction
