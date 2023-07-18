from lib.space import *

def test_space_creates_correctly():
    space1 = Space(1,"Space 1", "Nice space", 100, "01/01/23, 02/01/23, 03/01/23",1)
    assert space1.name == "Space 1"
    assert space1.description == "Nice space"

def test_identical_objects_are_equal():
    space1 = Space(1,"Space 1", "Nice space", 100, "01/01/23, 02/01/23, 03/01/23",1)
    space2 = Space(1,"Space 1", "Nice space", 100, "01/01/23, 02/01/23, 03/01/23",1)
    assert space1 == space2