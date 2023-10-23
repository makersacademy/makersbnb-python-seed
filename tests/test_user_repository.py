from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User

# Calling all() method lists all users
def test_all_method_lists_all_users(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'test-email-1', 'test-password-1'),
        User(2, 'test-email-2', 'test-password-2'),
        User(3, 'test-email-3', 'test-password-3')
    ]

# create() adds new user to database
def test_create_method_adds_new_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    repository.create(User(None, 'test-email-4', 'test-password-4'))
    users = repository.all()
    assert users == [
        User(1, 'test-email-1', 'test-password-1'),
        User(2, 'test-email-2', 'test-password-2'),
        User(3, 'test-email-3', 'test-password-3'),
        User(4, 'test-email-4', 'test-password-4')
    ]