from lib.user_repository import UserRepository
import pytest
from app import app


# test fixture to seed the database with data
def seed_item_repository(db_connection):
    db_connection.seed("seeds/makersbnb.sql")


# test fixture to create an instance of the repository
def repo_instance_constructor(db_connection):
    repo = UserRepository(db_connection)
    return repo


def test_create_adds_a_user_to_the_db(db_connection):
    seed_item_repository(db_connection)
    repo = repo_instance_constructor(db_connection)
    users = repo.all()
    user_length = len(users)
    repo.create_user("johnsmith", "john@email.com", "password@4")
    users = repo.all()
    assert len(users) == user_length + 1


# # test invalid password does not allow user creation
# def test_invalid_password(db_connection):
#     seed_item_repository(db_connection)
#     repo = repo_instance_constructor(db_connection)
#     users = repo.all()
#     print(users)
#     user_length = len(users)
#     repo.create_user("johnsmith", "john@email.com", "invalid")
#     users = repo.all()
#     assert len(users) == user_length


# test all() returns a list of users
def test_all_returns_a_list_of_users(db_connection):
    seed_item_repository(db_connection)
    repo = repo_instance_constructor(db_connection)
    users = repo.all()
    assert users is not None


def test_find_user_by_username(db_connection):
    seed_item_repository(db_connection)
    repo = repo_instance_constructor(db_connection)
    user = repo.find_user_by_username("TestUser1")
    assert user.username == "TestUser1"
