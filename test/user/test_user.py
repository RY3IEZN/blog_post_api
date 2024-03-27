from core.user.models import User


def test_create_user():
    user = User(username="testuser", email="user@email.com", hashed_password="password")
    assert user.username == "testuser"
    assert user.email == "user@email.com"
    assert user.hashed_password == "password"
