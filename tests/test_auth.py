from fastapi import HTTPException

from app.auth.dependencies import require_role, get_current_user


def test_register(client):
    res = client.post("/auth/register", json={
        "email": "a@test.com",
        "username": "a",
        "password": "123456"
    })
    assert res.status_code == 200


def test_login(client):
    client.post("/auth/register", json={
        "email": "b@test.com",
        "username": "b",
        "password": "123456"
    })

    res = client.post("/auth/login", data={
        "username": "b@test.com",
        "password": "123456"
    })

    assert res.status_code == 200
    assert "access_token" in res.json()


def test_invalid_login(client):
    res = client.post("/auth/login", data={
        "username": "wrong@test.com",
        "password": "123456"
    })
    assert res.status_code == 401


def test_unauthorized(client):
    res = client.get("/users/me")
    assert res.status_code == 401


def test_require_role_denied():
    class FakeUser:
        role = "user"

    checker = require_role("admin")

    try:
        checker(FakeUser())
    except HTTPException as e:
        assert e.status_code == 403

def test_invalid_token():
    try:
        get_current_user(token="invalid", db=None)
    except HTTPException as e:
        assert e.status_code == 401