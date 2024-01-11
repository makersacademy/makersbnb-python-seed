from lib.user import User, UserRepo
from unittest.mock import Mock

def test_creation_of_user():
    user = User(1, 'testuser', 'test@user.com', 'pass123', None)
    assert user.id == 1
    assert user.username == 'testuser'
    assert user.email == 'test@user.com'
    assert user.password == 'pass123'
    assert user.bookings == None
    user2 = User(1, 'testuser', 'test@user.com', 'pass123', None)
    assert user == user2

def test_is_valid_method_with_empty_strs():
    user = User(None, 'TestUsername', 'test@email.com', 'testpassword', None)
    assert user.is_valid()
    user = User(None, 'TestUsername', '', 'testpassword', None)
    assert not user.is_valid()
    user = User(None, '', '', '', None)
    assert not user.is_valid()

"""
Test username is only valid for letters and numbers and underscore, no spaces
or special chars
"""
def test_is_valid_method_usernames():
    user = User(None,  'TestUsername', 'test@email.com', 'testpassword', None)
    assert user.is_valid()
    user = User(None,  'Test_Username99', 'test@email.com', 'testpassword', None)
    assert user.is_valid()
    # space in user name is invalid
    user = User(None,  'Test Username', 'test@email.com', 'testpassword', None)
    assert not user.is_valid()
    # special char invalid
    user = User(None, 'Test$Username', 'test@email.com', 'testpassword', None)
    assert not user.is_valid()


def test_is_valid_on_emails():
    valid = [
        'joe_hello@hotmail.com',
        'tony89@gmail.com',
        'joe.hello@email.com',
        'tom.harry@cab.gov.uk',
        'tom.harry@gmail.gov.something.uk',
        'joe.hello.hello@something.com',
        'john@12345.com',
    ]
    invalid = [
        'joe%$@email.com',
        'joe hello@gov.uk',
        'john@hello',
        'joe-89@email.com',
        'hello',
        'hello@',
        '@.com',
        'hello@.com',
        'joe@hello..com',
        'joe.com',
        'joe@email.',
        'joe..hello@mail.com',
        '.hello@mail.com',
        'hello.@hotmail.com',
        'joe@@mail.com',
        'joe@hello.com.',
        'joe_hello@hotmail.co_m',
        'joe_hello@hotmail.1com',
    ]
    valid_tests = []
    for email in valid:
        user = User(None, 'TestUsername', email, 'testpassword', None)
        valid_tests.append(user.is_valid())
    assert valid_tests == [True]*7

    invalid_tests = []
    for email in invalid:
        user = User(None, 'TestUsername', email, 'testpassword', None)
        invalid_tests.append(user.is_valid())
    assert invalid_tests == [False]*18


# UserRepo class tests

def test_get_all_users(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    assert user_repo.get_all_users() == [
        User(1, 'test_username', 'test@test.com', 'password123', None),
        User(2, 'test_username2', 'test2@test.com', 'password123', None),
    ]


def test_find_user_by_id(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    assert user_repo.find_user_by_id(2) == User(2, 'test_username2', 'test2@test.com', 'password123', None)


def test_create_user(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    user = User(None, 'newuser', 'newuser@test.com', 'newpass', None)
    id = user_repo.create_user(user)
    assert user_repo.get_all_users() == [
        User(1, 'test_username', 'test@test.com', 'password123', None),
        User(2, 'test_username2', 'test2@test.com', 'password123', None),
        User(3, 'newuser', 'newuser@test.com', '253c2e786c2414dcaec8dbf11df515b5075371454b93a5687d24d96ddbf3b939', None)
    ]
    assert id == 3
    
def test_check_user(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    user = User(None, 'newuser', 'newuser@test.com', 'newpass', None) 
    assert user_repo.check_user(user)== []
    
def test_check_user_when_username_already_used(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    user = User(None, 'test_username2', 'newuser@test.com', 'newpass', None) 
    assert user_repo.check_user(user) == ['username: test_username2 is already in use']
    
def test_username_and_email_already_in_use(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    user = User(1, 'test_username', 'test@test.com', 'password123', None)
    assert user_repo.check_user(user) == ['username: test_username is already in use', "email: 'test@test.com' is already registered."]
    
    
def test_add_booking_to_user(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    booking = Mock()
    booking.id = 1
    booking.user_id = 2
    user_repo.add_booking(booking)
    assert user_repo.find_user_by_id(2) == User(2, 'test_username2', 'test2@test.com', 'password123', [1])

def test_add_multiple_bookings_to_user(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    booking = Mock()
    booking.id = 1
    booking.user_id = 2
    user_repo.add_booking(booking)
    booking2 = Mock()
    booking2.id = 2
    booking2.user_id = 2
    user_repo.add_booking(booking2)
    assert user_repo.find_user_by_id(2) == User(2, 'test_username2', 'test2@test.com', 'password123', [1, 2])


def test_find_user_by_username(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    assert user_repo.find_user_by_username('test_username2') == User(2, 'test_username2', 'test2@test.com', 'password123', None)


def test_check_password_correct(db_connection):
    db_connection.seed('seeds/bnb.sql')
    user_repo = UserRepo(db_connection)
    user = User(None, 'newuser', 'newuser@test.com', 'hello', None)
    user_repo.create_user(user)
    assert user_repo.check_password_correct('newuser', 'hello') == True

