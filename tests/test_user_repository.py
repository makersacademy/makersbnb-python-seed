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
    repository.create(User(None, 'test-email-4', 'test-password-4'))
    users = repository.all()
    assert users == [
        User(1, 'test-email-1', 'c2852cf707649f8392a055b4598e84206f13628b6f5807b1c8a6711b2598ef42'),
        User(2, 'test-email-2', '6eee3a5257a1329afe1dceb4ce1ebe0018e63a0788313253d3ec023228521ff2'),
        User(3, 'test-email-3', '187154941ec7f71e45f09cc85f5dc956329cee757bd1f8e1b1b2f34a4d7e0600'),
        User(4, 'test-email-4', '14b609f073d95e8c1472d314fb23215328608cc26f44a1ad0ba069978aea2a44')
    ]

