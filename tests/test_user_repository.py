from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User('Sam Morgan', 'sjmog', 'samm@makersacademy.com', 'password123'),
    ]

def create(self, User):
    self._connection.execute(
        "INSERT INTO user (name, username, email, password) values (%s, %s, %s, %s)",
        [User.name, User.username, User.email, User.password]
    )
    return None