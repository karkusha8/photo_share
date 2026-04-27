from app.services.photo import get_photos


def test_get_photos_sort_date(db):
    res = get_photos(db, sort="date")
    assert isinstance(res, list)