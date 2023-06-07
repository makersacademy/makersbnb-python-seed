from lib.user_repository import UserRepository
from lib.user import User

"""
Test that the user repository returns all the users
"""
def test_get_all_users(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    user_repository = UserRepository(db_connection)
    users = user_repository.all()
    assert users == [User(1, "testfirstname", "testlastname", "test@gmail.com", "test123"),
                    User(2, "Michael", "Jackson", "michael@gmail.com", "123456")]

"""
Test that a user is properly created
"""
def test_create_user(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    user_repository = UserRepository(db_connection)
    user = User(None, "Alfred", "Einstein", "a.einstein@gmail.com", "1234567")
    new_user = user_repository.create_user(user)
    assert new_user == User(3, "Alfred", "Einstein", "a.einstein@gmail.com", "1234567")
    assert user_repository.all() == [User(1, "testfirstname", "testlastname", "test@gmail.com", "test123"),
                                    User(2, "Michael", "Jackson", "michael@gmail.com", "123456"),
                                    User(3, "Alfred", "Einstein", "a.einstein@gmail.com", "1234567")]
    

"""
Test that the password is valid
"""    

def test_valid_password(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    repository = UserRepository(db_connection)
    assert True == repository.check_password("test@gmail.com", "test123")
    assert False == repository.check_password("bob@gmail.com", "falseemail")

"""
Find user, given their email
"""
def test_find_user_by_email(db_connection):
    db_connection.seed("seeds/users_spaces.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)
    user = repository.find_user_by_email("test@gmail.com")
    assert user == User(1, "testfirstname", "testlastname", "test@gmail.com", "test123")