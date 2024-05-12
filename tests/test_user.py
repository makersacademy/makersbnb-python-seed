from lib.user import *
import pytest
def test_usereq():
    user1 = User(1,'harry','password')
    user2 = User(1,'harry','password')
    assert user1 == user2

def test_usereq_noteq():
    user1 = User(1,'harry','password')
    user2 = User(2,'harry','password')
    assert user1 != user2

def test_user_repr():
    user1 = User(1,'harry','password')
    assert str(user1) == "User(1, harry, password)"


def test_isvalid_valid():
    user1 =  User(1,'harry','Password123!')
    assert user1.is_valid() == True

def test_isvalid_invalid_nocap():
    user1 =  User(1,'harry','password123!')
    assert user1.is_valid() == False

def test_isvalid_invalid_nospecial():
    user1 =  User(1,'harry','Password123')
    assert user1.is_valid() == False

def test_isvalid_invalid_tooshort():
    user1 =  User(1,'harry','pass123!')
    assert user1.is_valid() == False

'''

'''

def test_generate_errors_valid():
    user1 =  User(1,'harry','Password123!')
    assert user1.generate_errors() == None

def test_generate_errors_nocap():
    user1 =  User(1,'harry','password123!')
    assert user1.generate_errors() == "Passwords must include a Capital Letter"

def test_generate_errors_nospecial():
    user1 =  User(1,'harry','Password123')
    assert user1.generate_errors() == "Passwords must include one of the following special characters(! @ $ % &)"

def test_generate_errors_tooshort():
    user1 =  User(1,'harry','Pas123!')
    assert user1.generate_errors() == "Passwords must be 8 characters or longer"

