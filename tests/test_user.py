from lib.user import User

def test_setup(db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    newuser = User(db_connection, 'Jane@Janemail.com', 'Jan£Do£123')
    assert isinstance(newuser, User)
    k = db_connection.execute("SELECT name FROM USERS WHERE id = 5")
    assert k == [{'name': 'Jane@Janemail.com'}]
    assert newuser.id == 5