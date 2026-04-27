from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base


class Transform(Base):
    __tablename__ = "transforms"

    id = Column(Integer, primary_key=True, index=True)

    photo_id = Column(Integer, ForeignKey("photos.id"))

    transform_url = Column(String, nullable=False)
    qr_code = Column(String, nullable=False)