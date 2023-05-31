from lib.user import *

# 
def test_user_constructs():
    user = User(1, "Test username", "Test name", "test@test.com", "testpassword")
    assert user.id == 1
    assert user.username == "Test username"
    assert user.actualname == "Test name"
    assert user.email == "test@test.com"
    assert user.password == "testpassword"

"""
We can format users to strings nicely
# """
def test_users_format_nicely():
    user = User(1, "Test username", "Test name", "test@test.com", "testpassword")
    assert str(user) == "User(1, Test username, Test name, test@test.com, testpassword)"
#     # Try commenting out the `__repr__` method in lib/user.py
#     # And see what happens when you run this test again.

# """
# We can compare two identical users
# And have them be equal
# """
def test_users_are_equal():
    user1 = User(1, "Test username", "Test name", "test@test.com", "testpassword")
    user2 = User(1, "Test username", "Test name", "test@test.com", "testpassword")
    assert user1 == user2