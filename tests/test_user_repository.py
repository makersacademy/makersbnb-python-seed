from lib.User import User
from lib.UserRepository import UserRepository

def test_create_user(db_connection):
    db_connection.seed('seeds/database_setup.sql')
    repository = UserRepository(db_connection)
    repository.create_user(User(1,"username","password"))
    users = repository.all_users()
    
    assert users == [
        User(1,"username","password"),
    ]