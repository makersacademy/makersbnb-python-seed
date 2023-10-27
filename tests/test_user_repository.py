from lib.user import User
from lib.user_repository import UserRepository


def test_all_returns_list_of_users(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    
    result = repository.all()

    assert result == [
            User(1,'user1', 'user1email@example.com', 'password1'),
            User(2,'user2', 'user2email@example.com', 'password2'),
            User(3,'user3', 'user3email@example.com', 'password3'),
            User(4,'user4', 'user4email@example.com', 'password4'),
            User(5,'user5', 'user5email@example.com', 'password5'),
            User(6,'user6', 'user6email@example.com', 'password6'),
            User(7,'user7', 'user7email@example.com', 'password7'),
            User(8,'user8', 'user8email@example.com', 'password8'),
            User(9,'user9', 'user9email@example.com', 'password9'),
            User(10,'user10', 'user10email@example.com', 'password10')
    ]

def test_create(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    user = User(None, 'test_username', 'test_email', 'test_password')
    repository.create(user)
    assert repository.all() == [
        User(1,'user1', 'user1email@example.com', 'password1'),
            User(2,'user2', 'user2email@example.com', 'password2'),
            User(3,'user3', 'user3email@example.com', 'password3'),
            User(4,'user4', 'user4email@example.com', 'password4'),
            User(5,'user5', 'user5email@example.com', 'password5'),
            User(6,'user6', 'user6email@example.com', 'password6'),
            User(7,'user7', 'user7email@example.com', 'password7'),
            User(8,'user8', 'user8email@example.com', 'password8'),
            User(9,'user9', 'user9email@example.com', 'password9'),
            User(10,'user10', 'user10email@example.com', 'password10'),
            User(11, 'test_username', 'test_email', 'test_password')
    ]

def test_get_user_by_username(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = UserRepository(db_connection)
    result = repository.get_user_by_username('user2')
    assert result == User(2,'user2', 'user2email@example.com', 'password2')


