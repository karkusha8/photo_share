from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.photo import Photo
from app.services.transform import create_transform

router = APIRouter(prefix="/transforms", tags=["transforms"])


@router.post("/{photo_id}")
def create_transform_route(
    photo_id: int,
    db: Session = Depends(get_db)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        raise HTTPException(status_code=404, detail="Photo not found")

    return create_transform(db, photo)