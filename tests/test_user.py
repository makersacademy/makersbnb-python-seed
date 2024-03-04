from lib.user import User

"""
user constructs
id, username, password
"""

def test_user_constructs():
    user = User(1, "user1", "")
    assert user.id == 1
    assert user.username == "user1"
    assert user.password == ""

"""
when a user is created
we can retrieve it from the database
"""

def test_add_user(db_connection):
    db_connection.seed("makersbnb_test")
    user = User(db_connection)

    user.add(User(None, "user1", ""))
    result = user.id(1)
    assert result == User(1, "user1", "")


"""
when we create a user, 
its only in the format of an email address
"""

# def test_user_formats_nicely():
#     user = User(1, "user1", "")
#     assert str(user) == "User(1, user1, )"

