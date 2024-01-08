from lib.user import User

def test_user_construct():
    user = User("username", "email", 'password')
    assert user.username == "username"
    assert user.email == "email"
    assert user.password == 'password'

# test username is unique
    
# test email is valid
    
# test password is valid
    
# 