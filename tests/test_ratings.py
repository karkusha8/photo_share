import io
from tests.utils import get_token


def test_rating(client):
    token1 = get_token(client, "user1@test.com")
    token2 = get_token(client, "user2@test.com")

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token1}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    res = client.post(
        f"/ratings/{photo['id']}?value=5",
        headers={"Authorization": f"Bearer {token2}"}
    )

    assert res.status_code == 200


def test_rating_twice(client):
    token = get_token(client)

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    client.post(
        f"/ratings/{photo['id']}?value=5",
        headers={"Authorization": f"Bearer {token}"}
    )

    res = client.post(
        f"/ratings/{photo['id']}?value=4",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code in (400, 403)