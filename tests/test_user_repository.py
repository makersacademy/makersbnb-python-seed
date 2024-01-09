from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository.all()
We get a list of all the user accounts
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    
    users = repository.all()

    assert users == [User(1, 'Lil kim', 'femalerappers@femalerappers.com', 'apassword1@A'),
                    User(2, 'Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
                    User(3, 'Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*')
    ]

"""
When we call UserRepository.create()
A new user record is added to the database
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, 'Alan', 'test_email@test.com', '1Bcdefgh@'))

    assert repository.all() == [
                    User(1, 'Lil kim', 'femalerappers@femalerappers.com', 'apassword1@A'),
                    User(2, 'Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
                    User(3, 'Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*'),
                    User(4, 'Alan', 'test_email@test.com', '1Bcdefgh@')
    ]

"""
When we call UserRepository.find() with email and password
it returns true if in database, false if not
"""
def test_find_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find('dreamteam@barbiemail.com', 'ImjustKen123%*')

    assert user == True

