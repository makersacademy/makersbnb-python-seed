from lib.User.user_repository import UserRepository

'''
Check if user exists by username
'''
def test_user_exists(db_connection):
    db_connection.seed("seeds/usertable_connection.sql")
    repository = UserRepository(db_connection)
    assert repository.check('benhurst') == True
    assert repository.check('benhurst1234') == False


def test_user_verify_sql(db_connection):
    db_connection.seed("seeds/usertable_connection.sql")
    repository = UserRepository(db_connection) 

    assert repository.verify('ovie1234', '12345678') == {'id': 'rut9ehif', 'username': 'ovie1234', 'email': 'ovie@icloud.com', 'password': '12345678', 'phonenumber': '07764793090'}

