from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.auth.dependencies import get_current_user
from app.services.rating import create_rating

router = APIRouter(prefix="/ratings", tags=["ratings"])


@router.post("/{photo_id}")
def rate_photo(
    photo_id: int,
    value: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    if value < 1 or value > 5:
        raise HTTPException(status_code=400, detail="Rating must be 1-5")

    rating, error = create_rating(db, user.id, photo_id, value)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return rating