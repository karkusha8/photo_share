from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    text: str


class CommentUpdate(BaseModel):
    text: str


class CommentResponse(BaseModel):
    id: int
    text: str
    user_id: int
    photo_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True