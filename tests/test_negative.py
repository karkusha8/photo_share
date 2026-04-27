from tests.utils import get_token
from app.models.comment import Comment


def test_forbidden_delete_comment(client, db):
    token1 = get_token(client, "user1@test.com")
    token2 = get_token(client, "user2@test.com")

    photo = client.post(
        "/photos/",
        headers={"Authorization": f"Bearer {token1}"},
        files={"file": ("a.jpg", b"fake", "image/jpeg")}
    ).json()

    comment_res = client.post(
        f"/comments/{photo['id']}",
        headers={"Authorization": f"Bearer {token1}"},
        json={"text": "hi"}
    )

    assert comment_res.status_code == 200

    comment = db.query(Comment).first()
    assert comment is not None

    res = client.delete(
        f"/comments/{comment.id}",
        headers={"Authorization": f"Bearer {token2}"}
    )

    assert res.status_code == 403