from lib.user import User

def test_constructs_with_fields():
    user = User(1, "Example User", "examplepassword", "exampleemail@email.com")
    assert user.id == 1
    assert user.username == "Example User"
    assert user.user_password == "examplepassword"
    assert user.email == "exampleemail@email.com"

def test_equality():
    user1 = User(1, "Example User", "examplepassword", "exampleemail@email.com")
    user2 = User(1, "Example User", "examplepassword", "exampleemail@email.com")
    assert user1 == user2

def test_formatting():
    user = User(1, "Example User", "examplepassword", "exampleemail@email.com")
    assert str(user) == "User(1, Example User, examplepassword, exampleemail@email.com)"