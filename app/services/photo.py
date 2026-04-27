from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.photo import Photo
from app.models.tag import Tag
from app.models.rating import Rating


def create_photo(
    db: Session,
    user_id: int,
    url: str,
    public_id: str,
    description: str | None,
    tags: list[str]
):
    photo = Photo(
        url=url,
        public_id=public_id,
        description=description,
        owner_id=user_id
    )

    photo.tags = get_or_create_tags(db, tags)

    db.add(photo)
    db.commit()
    db.refresh(photo)

    return photo


def get_photos(
    db: Session,
    search: str | None = None,
    tag: str | None = None,
    sort: str | None = None
):
    query = db.query(Photo)


    if search:
        query = query.filter(Photo.description.ilike(f"%{search}%"))


    if tag:
        query = query.join(Photo.tags).filter(Tag.name == tag)

    photos = query.all()

    result = []
    for photo in photos:
        avg = db.query(func.avg(Rating.value)).filter(
            Rating.photo_id == photo.id
        ).scalar()

        photo.avg_rating = float(round(avg, 2)) if avg else 0.0
        result.append(photo)

    if sort == "rating":
        result.sort(key=lambda x: x.avg_rating, reverse=True)

    elif sort == "date":
        result.sort(key=lambda x: x.created_at, reverse=True)

    return result


def delete_photo(db: Session, photo_id: int):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        return None

    db.delete(photo)
    db.commit()

    return photo


def update_photo(db: Session, photo_id: int, description: str):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()

    if not photo:
        return None

    photo.description = description
    db.commit()
    db.refresh(photo)

    return photo


def get_or_create_tags(db: Session, tag_names: list[str]):
    tags = []

    for name in tag_names[:5]:  # максимум 5
        tag = db.query(Tag).filter(Tag.name == name).first()

        if not tag:
            tag = Tag(name=name)
            db.add(tag)
            db.commit()
            db.refresh(tag)

        tags.append(tag)

    return tags


def get_average_rating(db: Session, photo_id: int):
    avg = db.query(func.avg(Rating.value)).filter(
        Rating.photo_id == photo_id
    ).scalar()

    return float(round(avg, 2)) if avg else 0.0