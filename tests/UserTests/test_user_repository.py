from lib.User.user_repository import UserRepository

'''
Check if user exists by username
'''
def test_user_exists(db_connection):
    db_connection.seed("seeds/usertable_connection.sql")
    repository = UserRepository(db_connection)
    assert repository.check('benhurst') == True
    assert repository.check('benhurst1234') == False

