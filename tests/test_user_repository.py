from lib.user_repository import UserRepository
from lib.user import User

""" 
When I call all on the user repository
I get all the users back in a list
"""

def test_list_all_users(db_connection):
    db_connection.seed("seeds/blueberries_b&b.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
        User(1, 'blob@hotmail.com'),
        User(2, 'email3@email.com'),
        User(3, 'email2@hotmail.com'),
        User(4, 'email4@email.com')
    ]