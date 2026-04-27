from sqlalchemy import Column, Integer, ForeignKey
from app.database.db import Base


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)

    value = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))
    photo_id = Column(Integer, ForeignKey("photos.id"))