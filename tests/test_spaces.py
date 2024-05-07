from lib.spaces import *

"""
test the init 
"""

def test_construct_spaces():
    space = Space(1, 1, 'venue #1', 'desc #1', 50, True)
    assert space.id == 1
    assert space.owner == 1
    assert space.name == "venue #1"
    assert space.description == "desc #1"
    assert space.price_per_night == 50
    assert space.active == True


# def test_users_are_equal():
#     user1 = User(1, "test_email", "test_password")
#     user2 = User(1, "test_email", "test_password")
#     assert user1 == user2

# def test_user_are_format():
#     user = User(1, "test_email", "test_password")
#     assert str(user) == "User(1, test_email, test_password)"