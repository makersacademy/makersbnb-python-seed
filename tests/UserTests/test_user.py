from lib.User.user import User

def test_user_defines():
    user = User('benhurst', 'benhurst@email.com', '0123456789', 'password')
    assert user.username == 'benhurst'
    assert user.email == 'benhurst@email.com'
    assert user.phone_number == '0123456789'