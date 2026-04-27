from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.comment import CommentCreate, CommentResponse, CommentUpdate
from app.services.comment import create_comment, update_comment
from app.database.dependencies import get_db
from app.auth.dependencies import get_current_user
from app.models.comment import Comment

router = APIRouter(prefix="/comments", tags=["comments"])


@router.post("/{photo_id}", response_model=CommentResponse)
def create_comment_route(
    photo_id: int,
    data: CommentCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_comment(db, user.id, photo_id, data.text)


@router.put("/{comment_id}", response_model=CommentResponse)
def update_comment_route(
    comment_id: int,
    data: CommentUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if comment.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    return update_comment(db, comment, data.text)


@router.delete("/{comment_id}")
def delete_comment_route(
    comment_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    if user.role not in ["admin", "moderator"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(comment)
    db.commit()

    return {"message": "Comment deleted"}