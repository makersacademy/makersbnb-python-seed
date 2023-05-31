from lib.user import User

"""
User constructs with an id, name, email, password
"""

def test_user_constructs():
    user = User(id=1, name="test", email="tugrp@example.com", password="test")
    assert user.id == 1
    assert user.name == "test"
    assert user.email == "tugrp@example.com"
    assert user.password == "test"

"""
We can format users to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "test", "tugrp@example.com", "test")
    assert str(user) == "User(1, test, tugrp@example.com, test)"

"""
We can compare two identical user
And have them be equal
"""

def test_user_are_equal():
    user1 = User(1, "test", "tugrp@example.com", "test")
    user2 = User(1, "test", "tugrp@example.com", "test")
    assert user1 == user2
    
