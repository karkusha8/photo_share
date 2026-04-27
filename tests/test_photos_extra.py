import io
from tests.utils import get_token


def test_update_photo(client):
    token = get_token(client)

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    res = client.put(
        f"/photos/{photo['id']}",
        headers={"Authorization": f"Bearer {token}"},
        json={"description": "updated"}
    )

    assert res.status_code == 200


def test_search_and_tag(client):
    token = get_token(client)

    res = client.get("/photos/?search=test")
    assert res.status_code == 200

    res = client.get("/photos/?tag=cute")
    assert res.status_code == 200