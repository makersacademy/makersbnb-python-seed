from lib.user_repository import UserRepository
from lib.user import User


"""
when we call all,
we get a list of all users on the database
"""

def test_get_all_users(db_connection):
    db_connection.seed("ADD THIS")
    repo = UserRepository(db_connection)

    users = repo.all()

    assert users == [
        User(1, "user1@test.com", "password123")
    ]

"""
when a user is created
we can retrieve it from the database
"""

def test_add_user(db_connection):
    db_connection.seed("makersbnb_test")
    user = User(db_connection)

    user.add(User(None, "user1", "password123"))
    result = user.id(1)
    assert result == User(1, "user1", "password123")