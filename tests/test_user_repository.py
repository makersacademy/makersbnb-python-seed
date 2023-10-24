from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User
import hashlib

# Calling all() method lists all users
def test_all_method_lists_all_users(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'test-email-1', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42'),
        User(2, 'test-email-2', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2'),
        User(3, 'test-email-3', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600')
    ]

# create() adds new user to database
def test_create_method_adds_new_user(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    repository.create('test-email-4', 'test-password-4')
    users = repository.all()
    assert users == [
        User(1, 'test-email-1', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42'),
        User(2, 'test-email-2', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2'),
        User(3, 'test-email-3', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600'),
        User(4, 'test-email-4', '14b609f073d95e8c1472d314fb23215328608cc26f44a1ad0ba069978aea2a44')
    ]

# check_password() compares hashed password attempt vs stored hash for given email
# return true for password match
def test_check_password_method_returns_true(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    result = repository.check_password('test-email-1', 'test-password-1')
    assert result == True

# check_password() compares hashed password attempt vs stored hash for given email
# return false for password mismatch
def test_check_password_method_returns_false(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    result = repository.check_password('test-email-1', 'wrong_password')
    assert result == False

# find_by_email() returns correct user
def test_find_by_email(db_connection):
    db_connection.seed('seeds/users.sql')
    repository = UserRepository(db_connection)
    user = repository.find_by_email('test-email-1')
    assert user == User(1, 'test-email-1', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42')