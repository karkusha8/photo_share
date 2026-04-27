import io
from tests.utils import get_token


def test_comment_flow(client):
    token = get_token(client)

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    res = client.post(
        f"/comments/{photo['id']}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "nice"}
    )

    assert res.status_code == 200


def test_edit_comment(client):
    token = get_token(client)

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    comment = client.post(
        f"/comments/{photo['id']}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "hello"}
    ).json()

    res = client.put(
        f"/comments/{comment['id']}",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "updated"}
    )

    assert res.status_code == 200