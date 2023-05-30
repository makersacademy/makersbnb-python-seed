from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/User_seed.sql")
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
    
def test_get_email(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123')

# def test_get_by_email(db_connection):
#     db_connection.seed("seeds/user_seed.sql")
#     repository = UserRepository(db_connection)
#     expected_user = User(1, 'Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123')
#     result_user = repository.get_by_email('samm@makersacademy.com')
#     assert(result_user, expected_user)

