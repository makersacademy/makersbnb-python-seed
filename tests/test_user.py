from lib.user import User

'''
User constructs with a name, username, email and password
'''
def test_user_constructs():
    user = User(1, 'Test User', 'testusername', 'testemail@gmail.com', 'testpassword123')
    assert user.id == 1
    assert user.name == 'Test User'
    assert user.username == 'testusername'
    assert user.email == 'testemail@gmail.com'
    assert user.password == 'testpassword123'

'''
We can format users to strings nicely
'''
def test_users_format_nicely():
    user = User(1, 'Test User', 'testusername', 'testemail@gmail.com', 'testpassword123')
    assert str(user) == "User(id=1, name='Test User', username='testusername', email='testemail@gmail.com', password='testpassword123')"

'''
We can compare two identical albums
And have them be equal
'''
def test_users_are_equal():
    user_1 = User(1, 'Test User', 'testusername', 'testemail@gmail.com', 'testpassword123')
    user_2 = User(1, 'Test User', 'testusername', 'testemail@gmail.com', 'testpassword123')
    assert user_1 == user_2