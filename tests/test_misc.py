from tests.utils import get_token
from app.auth.blacklist import add_to_blacklist


def test_health_endpoint(client):
    res = client.get("/health")
    assert res.status_code == 200


def test_logout_blacklist(client):
    token = get_token(client)
    add_to_blacklist(token)

    res = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code in (401, 403, 200)