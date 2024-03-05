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



# def test_all(db_connection):
#     db_connection.seed("seeds/users.sql")
#     repo = UserRepository(db_connection)
#     all_users = repo.all()
#     assert all_users == [User(1, 'user1', 'user1@example.com', 'abc123'), User(2, 'user2', 'user2@yahoo.com', 'password123'), User(3, 'user3', 'user3@gmail.com', 'letmein!')]

# def test_all(db_connection):
#     db_connection.seed("seeds/users.sql")
#     pass

# def test_all(db_connection):
#     db_connection.seed("seeds/users.sql")
#     pass

# def test_all(db_connection):
#     db_connection.seed("seeds/users.sql")
#     pass