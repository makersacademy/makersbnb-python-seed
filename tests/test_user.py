from lib.user import User

"""
When a user is constructed
User's ID, username, email, password is initialized
"""
def test_user_initialized():
    user = User(1, "test_user", "test_email@test.com", "abcd123")
    assert user.id == 1
    assert user.user_name == "test_user"
    assert user.email == "test_email@test.com"
    assert user.password == "abcd123"

"""
When we compare two identical users
They evaluate as equal
"""
def test_user_equal():
    user_1 = User(1, "test_user", "test_email@test.com", "abcd123")
    user_2 = User(1, "test_user", "test_email@test.com", "abcd123")
    assert user_1 == user_2

