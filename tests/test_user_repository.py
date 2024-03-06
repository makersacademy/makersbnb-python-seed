from lib.user import User
from lib.user_repository import UserRepository

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/bnb_table.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all users

    # Assert on the results
    assert users== [
        User(1,'Adamexample@gmail.com', 'password123!'),
        User(2,'adam.takac24@outlook.com', 'Password456!'),
    ]

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = UserRepository(db_connection)

    booking = repository.find(2)
    assert booking == User(2,'adam.takac24@outlook.com', 'Password456!')

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = UserRepository(db_connection)

    repository.create(User(3,'new.email123@gmail.com', 'Newpassword$'))

    result = repository.all()
    assert result == [
        User(1,'adam.email@gmail.com', 'Password123!'),
        User(2,'example.email@outlook.com', 'Superpassword123!'),
        User(3,'new.email123@gmail.com', 'Newpassword$')
    ]

# """
# When we call UserRepository#delete
# We remove a record from the database.
# """
def test_delete_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        User(2,'example.email@outlook.com', 'Superpassword123!'),

    ]