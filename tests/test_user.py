import pytest
from lib.user import User

# When we create a user, it has an id, email and password:

def test_user_constructs():
    testuser = User(1, 'newuser@mail.com', 'testpassword1')
    assert testuser.email == 'newuser@mail.com'
    assert testuser.password == 'testpassword1'


# When we print an artist we get a readable string:
def test_user_outputs_well():
    testuser = User(1, 'newuser@mail.com', 'testpassword1')
    assert str(testuser) == 'User(1, newuser@mail.com, testpassword1)'