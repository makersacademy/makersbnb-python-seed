from lib.user import User

'''
User constructed with id and username
'''

def test_user_constructs():
    user = User(1, "testusername", "password")
    assert user.id == 1
    assert user.username == "testusername"
    assert user.password == "password"

'''
Formatting to string
'''

def test_user_formats_to_string_correctly():
    user = User(1, "testusername", "password")
    assert str(user) == "User(1, testusername, password)"

'''
Check to see two identical users are equal
'''

def test_users_are_equal():
    user1 = User(1, "testusername", "password")
    user2 = User(1, "testusername", "password")
    assert user1 == user2
