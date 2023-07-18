from lib.User import *

'''
constructs with an id, email and password
'''
def test_constructs():
    user = User(1, 'testemail', 'testpassword')
    assert user.id == 1
    assert user.email == 'testemail'
    assert user.password == 'testpassword'

'''
contents are equal
'''
def test_equal():
    user1 = User(1, 'testemail', 'testpassword')
    user2 = User(1, 'testemail', 'testpassword')
    assert user1 == user2

'''
represent users as string
'''
def test_return_a_string():
    user = User(1, 'testemail', 'testpassword')
    assert str(user) == "user(1, testemail, testpassword)"