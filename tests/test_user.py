from lib.user import User


def test_user_construct():
    user = User("username", "email@email.com", "password")
    assert user.username == "username"
    assert user.email == "email@email.com"
    assert user.password == "password"


# test username is unique
