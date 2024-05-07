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


def test_users_are_equal():
    space1 = Space(1, 1, 'venue #1', 'desc #1', 50, True)
    space2 = Space(1, 1, 'venue #1', 'desc #1', 50, True)
    assert space1 == space2

def test_user_are_format():
    space = Space(1, 1, 'venue #1', 'desc #1', 50, True)
    assert str(space) == "Space(1, 1, venue #1, desc #1, 50, True)"