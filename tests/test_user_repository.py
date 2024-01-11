from lib.user_repository import UserRepository
from lib.user import User

'''
Returns list of all users when all method is called.
'''

def test_all(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'user_1@mail.com', 'makersbnb2'),
        User(2, 'user_2@mail.com', 'qwerty123'),
        User(3, 'user_3@mail.com', 'makersbnb1')
    ]
    
'''
When I call the #create method 
I create a user in the database
And I can see it back in #all
'''

def test_create(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = UserRepository(db_connection)
    user = User(None, "new_user", "newpassword1234")
    repository.create(user)
    assert repository.all() == [
        User(1, 'user_1@mail.com', 'makersbnb2'),
        User(2, 'user_2@mail.com', 'qwerty123'),
        User(3, 'user_3@mail.com', 'makersbnb1'),
        User(4, 'new_user', 'newpassword1234')
    ]

def test_valid_signup(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = UserRepository(db_connection)
    result = repository.check_valid_signup('user_1@mail.com')
    assert result == False
    result = repository.check_valid_signup('Testemail@nomail.com')
    assert result == True

def test_valid_login(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = UserRepository(db_connection)
    result = repository.check_valid_login('user_1@mail.com','makersbnb2')
    assert result == True
    result = repository.check_valid_login('user_1@mail.com','makersbb2')
    assert result == False
    result = repository.check_valid_login('user1@mail.com','makersbnb2')
    assert result == False
