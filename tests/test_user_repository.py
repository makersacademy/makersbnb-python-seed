from lib.user import *
from lib.user_repository import *


def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    result = repository.all()
    assert result == [
            User('kathey.12@gmail.com', 'HElloworld1'),
            User('jen123@gmail.com', 'HElloworld2'),
            User('adrian@gmail.com', 'HElloworld3')
        ]