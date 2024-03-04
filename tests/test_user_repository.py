from lib.user_repository import UserRepository
from lib.user import User


"""
when we call all,
we get a list of all users on the database
"""
# come back and add database name 

def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb_test.sql")
    repo = UserRepository(db_connection)

    users = repo.all()

    assert users == [
        User(1, "user1@test.com", "password123"),
        User(2, "user2@test.com", "password000")
    ]

"""
when a single user is created
we can retrieve it from the database
"""

def test_add_user(db_connection):
    db_connection.seed("seeds/makersbnb_test.sql")
    user = UserRepository(db_connection)

    user.create(User(None, "user3@test.com", "password456"))
    result = user.all()
    
    assert result == [
        User(1, "user1@test.com", "password123"),
        User(2, "user2@test.com", "password000"),
        User(3, "user3@test.com", "password456"),
    ]


"""
when multiple users are created
we can retrieve them from the database
"""

def test_add_users(db_connection):
    db_connection.seed("seeds/makersbnb_test.sql")
    user = UserRepository(db_connection)

    user.create(User(None, "user3@test.com", "password456"))
    user.create(User(None, "user4@test.com", "password999"))
    result = user.all()

    assert result == [
        User(1, "user1@test.com", "password123"),
        User(2, "user2@test.com", "password000"),
        User(3, "user3@test.com", "password456"),
        User(4, "user4@test.com", "password999"),
    ]