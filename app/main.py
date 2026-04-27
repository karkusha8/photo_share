from fastapi import FastAPI

from app.database.db import Base, engine
import app.models

from app.routes import health, auth, users
from app.routes import photos, comments, ratings, transforms


app = FastAPI(
    title="PhotoShare API",
    description="API for photo sharing app",
    version="1.0.0"
)


app.include_router(health.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(photos.router)
app.include_router(comments.router)
app.include_router(ratings.router)
app.include_router(transforms.router)


@app.get("/")
def root():
    return {"message": "PhotoShare API is running 🚀"}