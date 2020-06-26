from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class UserInput(Base):
    __tablename__ = "user_inputs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)

    predictions = relationship("Prediction", back_populates="user_input")


class Prediction(Base):
    __tablename__="predictions"

    id = Column(Integer, primary_key=True, index=True)
    subreddit = Column(String)
    user_input = relationship("UserInput", back_populates="predictions")

