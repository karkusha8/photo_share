import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database.db import Base, engine
from app.database.db import SessionLocal


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(autouse=True)
def mock_cloudinary(monkeypatch):
    def fake_upload(file):
        return "http://test.com/image.jpg", "fake_id"

    monkeypatch.setattr(
        "app.routes.photos.upload_image",
        fake_upload
    )


@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)