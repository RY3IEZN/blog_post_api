from core.user.models import User
from core.post.models import Post


def test_create_post():
    post = Post(title="my first post", content="this is my post")
    assert post.title == "my first post"
    assert post.content == "this is my post"


def test_user_relationship():
    user = User(username="testuser", email="user@email.com", hashed_password="password")
    post = Post(title="my first post", content="this is my post", author=user)
    assert post.author == user
    assert user.posts == [post]
