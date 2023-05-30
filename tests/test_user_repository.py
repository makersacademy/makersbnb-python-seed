from lib.user_repository import *
from lib.user import User


def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all users

    # Assert on the results
    assert users == [
        User(1, "User1", "Actual Name 1", "user1@email.com", "Password1"),
        User(2, "User2", "Actual Name 2", "user2@email.com", "Password2"),
        User(3, "User3", "Actual Name 3", "user3@email.com", "Password3"),
    ]

def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "User4", "Actual Name 4", "user4@email.com", "Password4"))

    result = repository.all()
    assert result == [
        User(1, "User1", "Actual Name 1", "user1@email.com", "Password1"),
        User(2, "User2", "Actual Name 2", "user2@email.com", "Password2"),
        User(3, "User3", "Actual Name 3", "user3@email.com", "Password3"),
        User(4, "User4", "Actual Name 4", "user4@email.com", "Password4"),
    ]