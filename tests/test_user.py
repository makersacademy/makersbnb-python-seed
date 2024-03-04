from lib.user import *

def test_user_object_constructs():
    user = User('email_address1@gmail.com', 'username1', 'password1')
    assert user.email_address == 'email_address1@gmail.com'
    assert user.username == 'username1'
    assert user.password == 'password1'

def test_users_are_equal():
    user1 = User('email_address1@gmail.com', 'username1', 'password1')
    user2 = User('email_address1@gmail.com', 'username1', 'password1')
    assert user1 == user2