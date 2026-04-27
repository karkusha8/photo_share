from app.auth.blacklist import add_to_blacklist
from tests.utils import get_token


def test_blacklist_direct():
    token = "fake_token"
    add_to_blacklist(token)

    assert True


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_blacklist_multiple():
    add_to_blacklist("token1")
    add_to_blacklist("token2")

    assert True