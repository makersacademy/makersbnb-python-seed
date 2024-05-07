from lib.user import *
from lib.user_repository import *


def test_get_all_users(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = UserRepository(db_connection)

    result = repository.all()
    assert result == [
            User(1, 'test1@gmail.com', 'password123'),
            User(2, 'test2@gmail.com', 'password123'),
            User(3, 'test3@gmail.com', 'password123')
        ]
    
def test_create(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "test email", "Password1234"))
    result = repository.all()
    assert result == [
        User(1, 'test1@gmail.com', 'password123'),
        User(2, 'test2@gmail.com', 'password123'),
        User(3, 'test3@gmail.com', 'password123'),
        User(4, "test email", "Password1234")
    ]

def test_find(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = UserRepository(db_connection)
    result = repository.find(3)
    assert result == User(3, 'test3@gmail.com', 'password123')

def test_delete(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = UserRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        User(1, 'test1@gmail.com', 'password123'),
        User(2, 'test2@gmail.com', 'password123')
    ]