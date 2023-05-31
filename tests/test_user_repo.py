import pytest
from lib.userrepository import UserRepository
from lib.user import User

# When we call .get() on our userrepository we get a list of all the users

def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb_tables.sql")
    repo = UserRepository(db_connection)
    assert repo.get() == [
        User(1, 'mrtester@gmail.com', 'GudPass91!'),
        User(2, 'vlad@hotmail.com', 'Coolguy4')
    ]

# When we call create with a username and password the user is added to the database

def test_Can_Create(db_connection):
    db_connection.seed("seeds/makersbnb_tables.sql")
    repo = UserRepository(db_connection)
    testuser = User(1, 'newuser@mail.com', 'testpassword1')
    repo.create(testuser)
    assert repo.get() == [
        User(1, 'mrtester@gmail.com', 'GudPass91!'),
        User(2, 'vlad@hotmail.com', 'Coolguy4'),
        User(3, 'newuser@mail.com', 'testpassword1')
    ]