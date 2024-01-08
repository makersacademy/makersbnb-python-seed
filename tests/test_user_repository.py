from lib.user_repository import UserRepository

def test_create_adds_a_user_to_the_db(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = UserRepository(db_connection)
    users = repo.all()
    assert len(users) == 1
    repo.create_user('johnsmith', 'john@email.com', 'password@4')
    users = repo.all()
    assert len(users) == 2

# test all() returns a list of users