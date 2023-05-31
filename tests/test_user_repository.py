from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123'),
    ]

def test_add(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    user = User(None, 'Test Name', 'Test Username', 'Test Email', 'Test Password')
    repository.add(user)
    assert repository.all() == [
        User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123'),
        User(2, 'Test Name', 'Test Username', 'Test Email', 'Test Password')
        ]
    
def test_get_username(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    user = repository.get_by_username('sjmog')
    expected_user = User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123')
    assert user == expected_user

def test_get_email(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    user = repository.get_by_email('samm@makersacademy.com')
    expected_user = User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123')
    assert user == expected_user

def test_check_password(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    email = 'samm@makersacademy.com'
    password = 'password123'
    assert repository.check_password(email, password) is True

def test_query_username(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    existing_username = "sjmog"
    new_username = "new_user"
    existing_username_unique = repository.username_is_unique(existing_username)
    assert not existing_username_unique, f"Expected {existing_username} to be non-unique, but it is."
    new_username_unique = repository.username_is_unique(new_username)
    assert new_username_unique, f"Expected {new_username} to be unique, but it is not."

def test_query_email(db_connection):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)
    existing_email = "samm@makersacademy.com"
    new_email = "new@example.com"
    existing_email_unique = repository.email_is_unique(existing_email)
    assert not existing_email_unique, f"Expected {existing_email} to be non-unique, but it is."
    new_email_unique = repository.email_is_unique(new_email)
    assert new_email_unique, f"Expected {new_email} to be unique, but it is not."