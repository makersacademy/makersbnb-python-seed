from lib.space import *

def test_space_init():
    space = Space('name', 'description', 100, 'location', 45.0, 2)
    assert space.name == 'name'
    assert space.description == 'description'
    assert space.size == 100
    assert space.location == 'location'
    assert space.price == 45.0
    assert space.user_id == 2

def test_space_repr():
    space = Space('name', 'description', 100, 'location', 45.0, 2)
    assert str(space) == "name - location, £45.00"

def test_spaces_are_the_same():
    space1 = Space('name', 'description', 100, 'location', 45.0, 2)
    space2 = Space('name', 'description', 100, 'location', 45.0, 2)
    assert space1 == space2