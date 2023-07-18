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

def test_user_is_valid():
    assert User(1, "", "").is_valid() == False
    assert User(1, None, "").is_valid() == False
    assert User(1, "testemail", "").is_valid() == False
    assert User(1, "testemail", None).is_valid() == False
    assert User(1, None, "testpassword").is_valid() == False
    assert User(1, None, None).is_valid() == False
    assert User(1, "testemail", "testpassword").is_valid() == True
    assert User(None, "testemail", "testpassword").is_valid() == True

def test_user_errors():
    assert User(1,"","").raise_errors() == "fill in email, fill in password"
    assert User(1, "testemail", "").raise_errors() == "fill in password"
    assert User(1, "", "testpassword").raise_errors() == "fill in email"
    assert User(1, "", None).raise_errors() == "fill in email, fill in password"
    assert User(1, None, "").raise_errors() == "fill in email, fill in password"
    assert User(1, None, "testpassword").raise_errors() == "fill in email"
    assert User(1, "testemail", None).raise_errors() == "fill in password"
    assert User(1, "testemail", "testpassword").raise_errors() == None
    assert User(None, "testemail", "testpassword").raise_errors() == None
    

    