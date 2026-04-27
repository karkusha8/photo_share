import uuid

def get_token(client, email=None):
    if not email:
        email = f"{uuid.uuid4()}@test.com"

    client.post("/auth/register", json={
        "email": email,
        "username": email.split("@")[0],
        "password": "123456"
    })

    res = client.post("/auth/login", data={
        "username": email,
        "password": "123456"
    })

    return res.json()["access_token"]


def test_register(client):
    email = f"{uuid.uuid4()}@test.com"

    res = client.post("/auth/register", json={
        "email": email,
        "username": "a",
        "password": "123456"
    })
    assert res.status_code == 200


def test_login(client):
    email = f"{uuid.uuid4()}@test.com"

    client.post("/auth/register", json={
        "email": email,
        "username": "b",
        "password": "123456"
    })

    res = client.post("/auth/login", data={
        "username": email,
        "password": "123456"
    })

    assert res.status_code == 200
    assert "access_token" in res.json()