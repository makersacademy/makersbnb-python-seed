from lib.user_repository import UserRepository
from lib.user import User

"""
Test that the user repository returns all the users
"""
def test_get_all_users(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    user_repository = UserRepository(db_connection)
    users = user_repository.all()
    assert users == [User(1, "testfirstname", "testlastname", "test@gmail.com", "test123")]

"""
Test that a user is properly created
"""
def test_create_user(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    user_repository = UserRepository(db_connection)
    user = User(None, "Alfred", "Einstein", "a.einstein@gmail.com", "1234567")
    user_repository.create_user(user)
    assert user_repository.all() == [User(1, "testfirstname", "testlastname", "test@gmail.com", "test123"),
                                    User(2, "Alfred", "Einstein", "a.einstein@gmail.com", "1234567")]