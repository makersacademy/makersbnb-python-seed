from lib.user import User

def test_construct_user_with_name_email_password():
    user = User(1, 'user1', 'user1email@example.com', 'password1')
    assert user.id == 1
    assert user.username == 'user1'
    assert user.email == 'user1email@example.com'
    assert user.password == 'password1'