from lib.user import User

'''
Test User constructs with id, name, password and email
'''

def test_user_constructs():
    user = User(2, 'Aakash', 'P*ssword', 'Aakash@outllok.com')
    assert user.id == 2
    assert user.name == 'Aakash'
    assert user.password == 'P*ssword'
    assert user.email == 'Aakash@outllok.com'


'''
Test we can form users into nice strings
'''

def test_user_forms_nicely():
    user = User(2, 'Aakash', 'P*ssword', 'Aakash@outllok.com')
    assert str(user) == "User(2, Aakash, P*ssword, Aakash@outllok.com)"


'''
Test we can compare two identical users
and have them be equal 
'''

def test_users_to_be_equal():
    user1 = User(2, 'Aakash', 'P*ssword', 'Aakash@outllok.com')
    user2 = User(2, 'Aakash', 'P*ssword', 'Aakash@outllok.com')
    assert user1 == user2