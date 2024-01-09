from lib.user import User 

def test_user_constructors():
    space = User(1, "Test Username", "Test Password")
    assert space.id == 1
    assert space.username == "Test Username"
    assert space.password == "Test Password"

def test_identical_user():
    user1 = User(1, "Test Username", "Test Password")
    user2 = User(1, "Test Username", "Test Password")
    assert user1 == user2
