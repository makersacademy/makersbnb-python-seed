from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""

def test_get_all_records(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    assert repository.all() == [
      User(1, 'Oliver', 'oliver@test.com', 'password111!'),
      User(2, 'Kate', 'kate@test.com', 'password222!'),
      User(3, 'Joan', 'joan@test.com', 'password333$'),
      User(4, 'Saamiya', 'saamiya@test.com', 'password444$')
    ]

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_new_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "Joe", "Joe@test.com", "password2"))
    assert repository.all() == [
      User(1, 'Oliver', 'oliver@test.com', 'password111!'),
      User(2, 'Kate', 'kate@test.com', 'password222!'),
      User(3, 'Joan', 'joan@test.com', 'password333$'),
      User(4, 'Saamiya', 'saamiya@test.com', 'password444$'),
      User(5, 'Joe', 'Joe@test.com', 'password2')
    ]
   
# # When we call UserRepository#find
# # We get a single User object reflecting the seed data.
# # """
def test_get_single_record(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    user = repository.find(1)
    assert user == User(1, 'Oliver', 'oliver@test.com', 'password111!')


  

  