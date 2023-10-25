from lib.User.user_repository import UserRepository
from lib.User.user import User

'''
Check if user exists by username
'''
def test_user_exists(db_connection):
    db_connection.seed("seeds/usertable_connection.sql")
    repository = UserRepository(db_connection)
    assert repository.check('benhurst') == True
    assert repository.check('benhurst1234') == False

def test_create(db_connection):
    db_connection.seed("seeds/usertable_connection.sql")
    repository = UserRepository(db_connection)
    user = User('elon_musk', 'elonmusk@123.com', '0779874903', 'sillyman')
    repository.create(user)
    assert repository.check(user.username) == True