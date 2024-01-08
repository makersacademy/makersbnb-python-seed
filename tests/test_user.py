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