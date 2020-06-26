from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/requests/", response_model=models.RedditRequest)
def create_user(request: schemas.RedditRequestCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, request=request)


#@app.post("/predictions/", response_model=models.Item)
#def create_item_for_user(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    #return crud.create_user_item(db=db, item=item)

