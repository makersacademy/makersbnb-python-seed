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

def test_is_valid_username():
    validator1 = User(1,"Example User", "examplepassword", "exampleemail@email.com")
    assert validator1.is_valid_username() == True
    validator2 = User(1,"", "examplepassword", "exampleemail@email.com")
    assert validator2.is_valid_username() == False
    validator3 = User(1,None, "examplepassword", "exampleemail@email.com")
    assert validator3.is_valid_username() == False

def test_is_valid_password():
    validator1 = User(1,"Example User", "examplepassword", "exampleemail@email.com")
    assert validator1.is_valid_user_password() == True
    validator2 = User(1,"", "djdj", "exampleemail@email.com")
    assert validator2.is_valid_user_password() == False
    validator3 = User(1,None, "", "exampleemail@email.com")
    assert validator3.is_valid_user_password() == False

def test_generate_errors():
    validator1 = User(1,"", "exam", "exampleemail@email.com")
    assert validator1.generate_errors() == [
        "Username can't be blank",
        "Password must be at least 8 latters"
    ]
    validator2 = User(1,"sdfdsfds", "e", "exampleemail@email.com")
    assert validator2.generate_errors() == [
        "Password must be at least 8 latters"
    ]

