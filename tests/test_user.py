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
When two user items are identical
They evaluate as equal
"""


