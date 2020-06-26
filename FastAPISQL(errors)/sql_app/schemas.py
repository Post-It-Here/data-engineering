from typing import List

from pydantic import BaseModel

class RedditRequestBase(BaseModel):
    title: str
    description: str = None

class RedditRequestCreate(RedditRequestBase):
    pass

class SubredditPredictionsBase(BaseModel):
    subreddits: str

class SubredditPredictionsCreate(SubredditPredictionsBase):
    pass