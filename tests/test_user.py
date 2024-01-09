from lib.user import User

'''Constructs with id, email and password.
'''

def test_construction():
    user = User(1, "Test Email", "12345")
    assert user.id == 1
    assert user.email == "Test Email"
    assert user.passw == "12345"

