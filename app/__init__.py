from fastapi import FastAPI
from .routes.api_routes import Prediction, UserRequest, api_routes
app = FastAPI()

app.include_router(api_routes, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello World"}

