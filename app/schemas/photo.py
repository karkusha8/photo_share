from pydantic import BaseModel
from datetime import datetime


class PhotoCreate(BaseModel):
    url: str
    description: str | None = None
    tags: list[str] = []


class PhotoUpdate(BaseModel):
    description: str


class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class PhotoResponse(BaseModel):
    id: int
    url: str
    description: str | None
    owner_id: int
    created_at: datetime
    tags: list[TagResponse] = []
    avg_rating: float = 0

    class Config:
        from_attributes = True