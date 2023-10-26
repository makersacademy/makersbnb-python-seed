from lib.space import *

def test_space_initiated():
    space = Space(1, 'Beach house', 'Relaxing place', 210, 80, 1)
    assert space.id == 1
    assert space.name == "Beach house"
    assert space.description == "Relaxing place"
    assert space.size == 210
    assert space.price == 80
    assert space.owner_id == 1

def test_spaces_format_nicely():
    space = Space(1, "Beach house", "Relaxing place", 210, 80, 1)
    assert str(space) == "Space(1, Beach house, Relaxing place, 210, 80, 1)"

def test_spaces_are_equal():
    space1 = Space(1, "Beach house", "Relaxing place", 210, 80, 1)
    space2 = Space(1, "Beach house", "Relaxing place", 210, 80, 1)
    assert space1 == space2

