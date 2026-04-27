from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user, require_role
from app.database.dependencies import get_db
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    return user


@router.get("/admin-only")
def admin_only(user=Depends(require_role("admin"))):
    return {"message": f"Hello admin {user.username}"}


@router.get("/mod-only")
def mod_only(user=Depends(require_role("admin", "moderator"))):
    return {"message": f"Hello moderator {user.username}"}


@router.patch("/{user_id}/role")
def change_user_role(
    user_id: int,
    role: str,
    db: Session = Depends(get_db),
    admin=Depends(require_role("admin"))
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if role not in ["user", "moderator", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    if user.id == admin.id:
        raise HTTPException(status_code=400, detail="You cannot change your own role")

    user.role = role
    db.commit()
    db.refresh(user)

    return {"message": f"User role updated to {role}"}


@router.patch("/{user_id}/ban")
def ban_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("admin"))
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = False
    db.commit()

    return {"message": "User banned"}


@router.patch("/{user_id}/unban")
def unban_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_role("admin"))
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_active = True
    db.commit()

    return {"message": "User unbanned"}


@router.get("/{username}")
def get_user_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active
    }