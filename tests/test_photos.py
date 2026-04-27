import io
from tests.utils import get_token


def test_upload_photo(client):
    token = get_token(client)

    file = io.BytesIO(b"fake image")

    res = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("test.jpg", file, "image/jpeg")}
    )

    assert res.status_code == 200


def test_get_photos(client):
    res = client.get("/photos/")
    assert res.status_code == 200


def test_delete_other_user(client):
    token1 = get_token(client, "user1@test.com")
    token2 = get_token(client, "user2@test.com")

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token1}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    res = client.delete(
        f"/photos/{photo['id']}",
        headers={"Authorization": f"Bearer {token2}"}
    )

    assert res.status_code == 403