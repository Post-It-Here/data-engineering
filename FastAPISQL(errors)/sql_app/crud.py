from sqlalchemy.orm import Session

from . import models, schemas

def create_reddit_request(db: Session, redditrequest: schemas.RedditRequestCreate):
    db_request = models.RedditRequest()
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def create_subreddit_predictions(db: Session, subredditpredictions: schemas.SubredditPredictionsCreate):
    db_pred = models.SubredditPredictions()
    db.add(db_pred)
    db.commit()
    db.refresh(db_pred)
    return db_pred