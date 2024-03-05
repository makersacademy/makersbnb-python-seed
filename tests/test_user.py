from lib.user import User

"""
user constructs
id, username, password
"""

def test_user_constructs():
    user = User(1, "user1@test.com", "password123")
    assert user.id == 1
    assert user.username == "user1@test.com"
    assert user.password == "password123"

"""
when we create a user, 
its only in the format of an email address
"""

def test_username_is_email():
    user = User(1, "user1@test.com", "password123")
    assert user.username == "user1@test.com"

"""
when we create a user,
if we have the same user, 
it returns that they are equal
"""

def test_users_are_equal():
    user1 = User(1, "user1", "password")
    user2 = User(1, "user1", "password")
    assert user1 ==  user2

