from lib.user import *

user = User(1,'FName', 'LName', 'email@email.com', '01234567890', 'password')

def test_user_constructs():
    assert user.id == 1
    assert user.first_name == 'FName'
    assert user.last_name == 'LName'
    assert user.email == 'email@email.com'
    assert user.telephone_number == '01234567890'
    assert user.password == 'password'