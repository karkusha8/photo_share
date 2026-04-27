from app.services.photo import create_photo, get_photos, delete_photo, update_photo
from app.models.user import User


def test_create_and_delete_photo(db):
    user = User(
        email="test@test.com",
        username="test",
        password="123",
        role="user",
        is_active=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    photo = create_photo(
        db=db,
        user_id=user.id,
        url="http://test.com/img.jpg",
        public_id="test_id",
        description="test",
        tags=[]
    )

    assert photo.id is not None

    deleted = delete_photo(db, photo.id)
    assert deleted is not None

def test_get_photos_no_sort(db):
    res = get_photos(db, sort=None)
    assert isinstance(res, list)


def test_get_photos_all_branches(db):
    res = get_photos(
        db,
        search="test",
        tag="tag",
        sort="rating"
    )
    assert isinstance(res, list)

    res = get_photos(
        db,
        search=None,
        tag=None,
        sort="date"
    )
    assert isinstance(res, list)