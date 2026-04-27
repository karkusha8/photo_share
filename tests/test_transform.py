import io
from tests.utils import get_token


def test_create_transform(client):
    token = get_token(client)

    file = io.BytesIO(b"fake")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token}"},
        files={"file": ("a.jpg", file, "image/jpeg")}
    ).json()

    res = client.post(
        f"/transforms/{photo['id']}",
        headers={"Authorization": f"Bearer {token}"},
        params={"transform_url": "http://test.com/img.jpg"}
    )

    assert res.status_code == 200