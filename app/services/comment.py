from sqlalchemy.orm import Session
from datetime import datetime, UTC
from app.models.comment import Comment


def create_comment(db: Session, user_id: int, photo_id: int, text: str):
    comment = Comment(
        text=text,
        user_id=user_id,
        photo_id=photo_id
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def update_comment(db: Session, comment: Comment, text: str):
    comment.text = text
    comment.updated_at = datetime.now(UTC)

    db.commit()
    db.refresh(comment)

    return comment