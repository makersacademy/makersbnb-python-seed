from lib.user_repository import *
from lib.user import User


def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all users

    # Assert on the results
    assert users == [
        User(1, "User1", "Actual Name 1", "user1@email.com", "19513fdc9da4fb72a4a05eb66917548d3c90ff94d5419e1f2363eea89dfee1dd"),
        User(2, "User2", "Actual Name 2", "user2@email.com", "1be0222750aaf3889ab95b5d593ba12e4ff1046474702d6b4779f4b527305b23"),
        User(3, "User3", "Actual Name 3", "user3@email.com", "2538f153f36161c45c3c90afaa3f9ccc5b0fa5554c7c582efe67193abb2d5202"),
    ]

def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "User4", "Actual Name 4", "user4@email.com", "Password4"))

    result = repository.all()
    assert result == [
        User(1, "User1", "Actual Name 1", "user1@email.com", "19513fdc9da4fb72a4a05eb66917548d3c90ff94d5419e1f2363eea89dfee1dd"),
        User(2, "User2", "Actual Name 2", "user2@email.com", "1be0222750aaf3889ab95b5d593ba12e4ff1046474702d6b4779f4b527305b23"),
        User(3, "User3", "Actual Name 3", "user3@email.com", "2538f153f36161c45c3c90afaa3f9ccc5b0fa5554c7c582efe67193abb2d5202"),
        User(4, "User4", "Actual Name 4", "user4@email.com", "db514f5b3285acaa1ad28290f5fefc38f2761a1f297b1d24f8129dd64638825d"),
    ]

def test_check_password(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    repo.create(User(None, "User4", "Actual Name 4", "user4@email.com", "Password4"))
    assert repo.check_password("User4", "Password4") == True

