from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123'),
        User(2, 'Owner McOwner', 'owner', 'owner@email.com', 'password123'),
    ]

def create(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    user = User(2, 'Test Name', 'Test Username', 'Test Email', 'Test Password')
    repository.create(user)
    assert repository.all() == [
        User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123'),
        User(2, 'Owner McOwner', 'owner', 'owner@email.com', 'password123'),
        User(3, 'Test Name', 'Test Username', 'Test Email', 'Test Password')
        ]