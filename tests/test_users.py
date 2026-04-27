from tests.utils import get_token


def test_get_me(client):
    token = get_token(client)

    res = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res.status_code == 200


def test_admin_only_denied(client):
    admin_token = get_token(client, "admin@test.com")

    user_token = get_token(client, "user@test.com")

    res = client.get(
        "/users/admin-only",
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 403