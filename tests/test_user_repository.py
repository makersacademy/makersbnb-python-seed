from lib.user_repository import UserRepository
from lib.user import User

"""
We can call #UserRepository and
We get all the seed data back
"""

def test_get_all_users(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)

    user = repository.all()

    assert user == [
        User(1, 'user1', 'password1'),
        User(2, 'user2', 'password2'),
        User(3, 'user3', 'password3')
    ]

"""
when given user1 and password1
we can return this 'This password is correct!'
"""
def test_find_user(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    user = repository.find_one_user(1)
    assert user == User(1, 'user1', 'password1')

def test_validate_specfic_username(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    password = repository.validate_specfic_username('user1')
    assert password == 'password1' 

def test_validate_specfic_password(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    username = repository.validate_specfic_password('password1')
    assert username == 'user1' 

def test_check_if_username_and_password_are_connected(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    result = repository.check_user_login('user1', 'password1')
    assert result == 'This password is correct!'

def test_check_if_password_is_incorrect(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    result = repository.check_user_login('user1', 'password15')
    assert result == 'Incorrect password! Please try again.'

def test_check_if_username_is_incorrect(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    result = repository.check_user_login('user15', 'password1')
    assert result == 'Username not found'

# def test_get_user_login(db_connection):
#     db_connection.seed('seeds/bnb.sql')
#     repository = UserRepository(db_connection)

#     user = repository.user_login('user1', 'password1')

#     assert user == 'This password is correct!'

