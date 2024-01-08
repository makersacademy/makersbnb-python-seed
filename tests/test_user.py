from lib.user import User, UserRepo

def test_creation_of_user():
    user = User(1, 'testuser', 'test@user.com', 'pass123', None)
    assert user.id == 1
    assert user.username == 'testuser'
    assert user.email == 'test@user.com'
    assert user.password == 'pass123'
    assert user.bookings == None
    user2 = User(1, 'testuser', 'test@user.com', 'pass123', None)
    assert user == user2




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
        User(3, 'newuser', 'newuser@test.com', 'newpass', None)
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
    
    
    