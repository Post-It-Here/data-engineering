from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class RedditRequest(Base):
    __tablename__ = "reddit_request"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    #responses = relationship("SubredditPredictions", back_populates="titles")


class SubredditPredictions(Base):
    __tablename__ = "subreddit_predictions"

    id = Column(Integer, primary_key=True, index=True)
    subreddits = Column(String, index=True)

    #titles = relationship("RedditRequest", back_populates="responses")