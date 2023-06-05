import pytest
from lib.user import User 

def test_constructs():
    user = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    assert user.id == 1
    assert user.first_name == 'firstname'
    assert user.last_name == 'lastname'
    assert user.email == 'test@test.com'
    assert user.password == 'password'

def test_users_are_equal():
    user1 = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    user2 = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    assert user1 == user2


def test_posts_format_nicely():
    user = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    assert str(user) == "User(1, firstname, lastname, test@test.com, password)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.
