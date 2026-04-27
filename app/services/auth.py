from sqlalchemy.orm import Session
from app.models.user import User
from app.auth.security import hash_password, verify_password


def create_user(db: Session, email: str, username: str, password: str):
    users_count = db.query(User).count()

    role = "admin" if users_count == 0 else "user"

    user = User(
        email=email,
        username=username,
        password=hash_password(password),
        role=role
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user