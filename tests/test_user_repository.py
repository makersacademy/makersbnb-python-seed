from lib.user import User
from lib.user_repository import UserRepository

"""
When we call UserRepository #all
We get a list of User objects reflecting the seed data
"""

def test_get_all_users(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)

    users = repository.all()
    assert users == [
        User(1,'Alex', 'Adams', 'email1@email.com', '01234567891', 'password1'),
        User(2,'Charlie', 'Smith', 'email2@email.com', '01234567892', 'password2'),
        User(3,'Jamie', 'Brown', 'email3@email.com', '01234567893', 'password3'),
    ]

def test_create(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None,'name1','name2','email4@email.com', '01234567894', 'password4'))
    users = repository.all()
    assert users == [
        User(1,'Alex', 'Adams', 'email1@email.com', '01234567891', 'password1'),
        User(2,'Charlie', 'Smith', 'email2@email.com', '01234567892', 'password2'),
        User(3,'Jamie', 'Brown', 'email3@email.com', '01234567893', 'password3'),
        User(4,'name1', 'name2','email4@email.com','01234567894','password4')
    ]

def test_find_user(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user(1)
    assert user == User(1,'Alex', 'Adams', 'email1@email.com', '01234567891', 'password1')