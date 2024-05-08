from lib.User import User
from lib.UserRepository import UserRepository

def test_create_user(db_connection):
    db_connection.seed('seeds/database_setup.sql')
    repository = UserRepository(db_connection)
    repository.create_user(User(1,"username","password"))
    users = repository.all()
    
    assert users == [
        User(1,"username","password"),
    ]

def test_list_all_users(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result ==[
        User(1, 'Andrew', 'Password1!'),
        User(2, 'Benedict', 'Password2!'),
        User(3, 'Melissa', 'Password3!'),
        User(4, 'Umut', 'Password4!'),
        User(5, 'Tomi', 'Password5!'),
        User(6, 'Jawad', 'Password6!')
    ]
        