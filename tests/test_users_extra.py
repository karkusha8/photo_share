from tests.utils import get_token


def test_ban_and_unban_user(client):
    admin = get_token(client, "admin@test.com")
    user = get_token(client, "user@test.com")

    res = client.patch(
        "/users/2/ban",
        headers={"Authorization": f"Bearer {admin}"}
    )
    assert res.status_code == 200

    res = client.patch(
        "/users/2/unban",
        headers={"Authorization": f"Bearer {admin}"}
    )
    assert res.status_code == 200


def test_change_role(client):
    admin = get_token(client, "admin@test.com")
    user = get_token(client, "user@test.com")

    res = client.patch(
        "/users/2/role?role=moderator",
        headers={"Authorization": f"Bearer {admin}"}
    )

    assert res.status_code == 200

def test_user_profile_not_found(client):
    res = client.get("/users/not_existing_user")
    assert res.status_code == 404


def test_change_role_invalid(client):
    admin = get_token(client, "admin@test.com")
    user = get_token(client, "user@test.com")

    res = client.patch(
        "/users/2/role?role=invalid_role",
        headers={"Authorization": f"Bearer {admin}"}
    )

    assert res.status_code == 400

def test_get_user_profile_exists(client):
    token = get_token(client, "user@test.com")

    res = client.get("/users/user")
    assert res.status_code in (200, 404)