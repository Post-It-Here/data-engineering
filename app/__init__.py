from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

from .routes.api_routes import api_routes

app = FastAPI(
    title="Post it Here",
    description="An API that receives user input via POST and returns the most compatible subreddits to post it on!",
    version="0.1.0",
)

app.include_router(api_routes, prefix="/api")


@app.get("/")
async def root():
    """Redirects to documentation"""
    return RedirectResponse("/docs", status.HTTP_303_SEE_OTHER)
