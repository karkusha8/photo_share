from sqlalchemy.orm import Session
from app.models.rating import Rating
from app.models.photo import Photo


def create_rating(db: Session, user_id: int, photo_id: int, value: int):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()
    if photo.owner_id == user_id:
        return None, "Cannot rate your own photo"

    existing = db.query(Rating).filter(
        Rating.user_id == user_id,
        Rating.photo_id == photo_id
    ).first()

    if existing:
        return None, "Already rated"

    rating = Rating(
        value=value,
        user_id=user_id,
        photo_id=photo_id
    )

    db.add(rating)
    db.commit()
    db.refresh(rating)

    return rating, None