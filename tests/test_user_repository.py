from lib.user_repository import UserRepository
from lib.user import User
from lib.database_connection import DatabaseConnection

def test_find_record_correct_username_and_password(db_connection):
    db_connection.seed("seeds/users.sql")
    repo = UserRepository(db_connection)
    user = repo.find("user1", "abc123")
    assert user == True

def test_find_record_incorrect_username(db_connection):
    db_connection.seed("seeds/users.sql")
    repo = UserRepository(db_connection)
    user = repo.find("rachel", "abc123")
    assert user == False

def test_find_record_incorrect_password(db_connection):
    db_connection.seed("seeds/users.sql")
    repo = UserRepository(db_connection)
    user = repo.find("user1", "abc1234")
    assert user == False

def test_find_record_correct_in_different_records(db_connection):
    db_connection.seed("seeds/users.sql")
    repo = UserRepository(db_connection)
    user = repo.find("user2", "abc123")
    assert user == False

