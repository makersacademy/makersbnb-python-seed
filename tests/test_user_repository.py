# File: tests/test_user_repository.py
from lib.user_repository import UserRepository
from lib.user import User

"""
Test we can retrieve all users
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    users = repo.all()

    assert users == [User('user_1', 'space_1'),
                     User('user_2', 'space_2')]


"""
Test we can find specific users using a user ID
"""
def test_find_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    users = repo.all()
    print(users)
    user = repo.find(2)
    print(user.id)
    assert user.username == "user_2"
    assert user == User("user_2", "space_2", id=2)


"""
Test we can create specific a user
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)

    new_user = User('New user', '')
    users = repo.create(new_user)

    users = repo.all()
    assert users == [
                    User('user_1', 'space_1'),
                    User('user_2', 'space_2'),
                    User('New user', '')
                    ]