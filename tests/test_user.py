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

"""
We can assess a user for validity
"""
def test_user_validity():
    assert User(1, "", "", "", "").is_valid() == False
    assert User(1, "Name", "", "", "").is_valid() == False
    assert User(1, "", "Last Name", "", "").is_valid() == False
    assert User(1, "Name", None, "", "").is_valid() == False
    assert User(1, None, "Last Name", None, None).is_valid() == False
    assert User(1, "Name", "Last Name", "test@email.com", "").is_valid() == False
    assert User(1, None, None, "email@gmail.com", "test_password").is_valid() == False
    assert User(1, "Name", "Email@email.com", "test_user_name", "test_password").is_valid() == True
    assert User(None, "Name", "Email@email.com", "test_user_name", "test_password").is_valid() == True

"""
We can generate errors for an invalid user
"""
def test_user_errors():
    assert User(1, "", "", "", "").generate_errors() == \
        "First Name can't be blank, Last Name can't be blank, Email can't be blank, Password can't be blank"
    assert User(1, "First Name", "", "", "").generate_errors() == \
        "Last Name can't be blank, Email can't be blank, Password can't be blank"
    assert User(1, "", "Last Name", "", "").generate_errors() == \
        "First Name can't be blank, Email can't be blank, Password can't be blank"
    assert User(1, "First Name", None, "Email", "password_test").generate_errors() == "Last Name can't be blank"
    assert User(1, None, "Last Name", "Email_test", "password_test").generate_errors() == "First Name can't be blank"
    assert User(1, "First Name", "Last Name", "Email_test", "password_test").generate_errors() == None
    assert User(None, "First Name", "Last Name", "Email_test", "password_test").generate_errors() == None

def test_users_are_equal():
    user1 = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    user2 = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    assert user1 == user2

def test_posts_format_nicely():
    user = User(1, 'firstname', 'lastname', 'test@test.com', 'password')
    assert str(user) == "User(1, firstname, lastname, test@test.com, password)"