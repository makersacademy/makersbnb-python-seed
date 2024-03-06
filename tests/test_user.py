from lib.user import User

""" 
When I construct a user 
With the fields id and email
They are reflected in the instance properties
"""

def test_constructs_with_fields():
    user = User(1,'blob@hotmail.com')
    assert user.email == 'blob@hotmail.com'


def test_users_format_nicely():
    user = User(1, "blob@hotmail.com")
    assert str(user) == "User(blob@hotmail.com)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_users_are_equal():
    user1 = User(6, "Test email")
    user2 = User(6, "Test email")
    assert user1 == user2