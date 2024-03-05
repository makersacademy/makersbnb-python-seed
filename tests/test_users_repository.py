from lib.user import *
from lib.users_repository import *
import pytest

"""
When we seed UsersRepository 
Data returned is inline with the seed file
"""
def test_db_connection(db_connection):
    db_connection.seed("seeds/bnb.sql")
    connection = UsersRepository(db_connection)
    assert connection is not None

"""
When we call UsersRepository #find
We get a single User object reflecting the seed data.
"""
def test_get_single_user_record(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = UsersRepository(db_connection)
    user = repository.find("user123@gmail.com")
    assert user == User(4, 'user123@gmail.com', 'Emily', 'Johnson', '03123456789', 'SecretPass123')

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = UsersRepository(db_connection)

    repository.create(User(None, 'fgtg@example.com', 'FG', 'TG', '6666666666', '@12Cupoftea34as'))

    result = repository.find('fgtg@example.com')
    print(result)
    assert result == User(7, 'fgtg@example.com', 'FG', 'TG', '6666666666', '@12Cupoftea34as')

"""
When we call UsersRepository #find with an email address that doesn't exist
We get an error 
"""
def test_get_error_no_matching_record(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = UsersRepository(db_connection)
    with pytest.raises(EmailNotFound) as e:
        repository.find("user5888536123@gmail.com")
    error_message = str(e.value)
    assert error_message == "User not found"

    """
When we call UsersRepository #create to add a new user with an email address exists
We get an error 
"""
def test_non_unique_email(db_connection):

    db_connection.seed("seeds/bnb.sql")
    repository = UsersRepository(db_connection)

    result = repository.create(User(None, 'user123@gmail.com', 'FG', 'TG', '6666666666', '@12Cupoftea34as'))
    print(result)
    assert result == "Email already assigned to an account!"