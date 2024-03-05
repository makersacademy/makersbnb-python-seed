from lib.user_repository import UserRepository
from lib.user import User


'''
Test connection between conftest.py and lib
'''

def test_find(db_connection):
    db_connection.seed("seeds/Users.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, 'Aakash', 'P*ssword', 'Aakash@outllok.com')


def test_create(db_connection):
    db_connection.seed("seeds/Users.sql")
    repository = UserRepository(db_connection)


    user = repository.create(User(None, 'John', '12345', 'John@outlook.com'))
    result = repository.find(user.id)
    assert result == user