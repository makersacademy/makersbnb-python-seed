from lib.user import *
import pytest

"""
User constructs with an id, email, first name, last name, phone number, and password
"""
def test_user_constructs():
    user = User(1, "test@email.com", "Joe", "Blogs", "01234567890", "P4ssword?")
    assert user.id == 1
    assert user.email == "test@email.com"
    assert user.first_name == "Joe"
    assert user.last_name == "Blogs"
    assert user.phone_number == "01234567890"
    assert user.password == "P4ssword?"

"""
We can format user to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "test@email.com", "Joe", "Blogs", "01234567890", "P4ssword?")
    assert str(user) == "User(1, test@email.com, Joe, Blogs, 01234567890, P4ssword?)"

"""
We can compare two identical users
And have them be equal
"""
def test_artists_are_equal():
    user1 = User(1, "test@email.com", "Joe", "Blogs", "01234567890", "P4ssword?")
    user2 = User(1, "test@email.com", "Joe", "Blogs", "01234567890", "P4ssword?")
    assert user1 == user2

"""
User constructs with all criteria, except password not to requirements
Return Error message.
"""
def test_password_error_not_matching_criteria():
    user = User(1, "test@email.com", "Joe", "Blogs", "01234567890", "password")
    with pytest.raises(InvalidPassword) as e:
        user.password_validator()
    error_message = str(e.value)
    assert error_message == "Password not OK"

"""
New user constructed with phone number including white space.
Returns amend phone number with no white space.
"""
def test_white_space_removal_from_phone_number():
    user = User(1, "test@email.com", "Joe", "Blogs", "01234 567 890", "P4ssword?")
    assert user.phone_number == "01234567890"

"""
New user constructed with capitalised email address.
Returns lowercase email address
"""
def test_lowercase_email_formatting():
    user = User(1, "TEST@EMAIL.COM", "Joe", "Blogs", "01234567890", "P4ssword?")
    assert user.email == "test@email.com"


