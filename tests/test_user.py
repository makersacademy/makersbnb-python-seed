from lib.user import *
import pytest

"""
Given both password and username are valid, no exception is raised
"""
def test_with_valid_password_and_username():
    user = User(None, 'adam.email@gmail.com', 'Password123!')
    assert user.user_name == 'adam.email@gmail.com'
    assert user.user_password == 'Password123!'

"""
Given the password is too short, a ValueError is raised
"""
def test_with_short_password():
    with pytest.raises(ValueError) as e:
        User(None, 'adam.email@gmail.com', 'Short1!')
    error_message = str(e.value)
    assert error_message == "Password does not meet the criteria, password needs to be 8 characters long and contain a special character"


"""
Given the username is an invalid email, a ValueError is raised
"""
def test_with_invalid_email():
    with pytest.raises(ValueError) as exc_info:
        User(None, 'invalid-email', 'Password123!')
    assert "Invalid username format, enter your email address"

"""
Given the password lacks special characters, a ValueError is raised
"""
def test_with_password_missing_special_characters():
    with pytest.raises(ValueError) as exc_info:
        User(None, 'adam.email@gmail.com', 'Password123')
    assert "Password does not meet the criteria, password needs to be 8 characters long and contain a special character" 

"""
Given the password is valid but the email is invalid, a ValueError is raised
"""
def test_with_valid_password_invalid_email():
    with pytest.raises(ValueError) as exc_info:
        User(None, 'adam.email', 'Password123!')
    assert "Invalid username format, enter your email address" 
