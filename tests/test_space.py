from lib.space import *

def test_construct():
    space = Space(1, "test description", 99.99, 1, "test name")
    assert space.id == 1
    assert space.description == "test description"
    assert space.price == 99.99
    assert space.user_id == 1
    assert space.name == "test name"

def test_format():
    space = Space(1, "test description", 99.99, 1, "test name")
    assert str(space) == 'Space(1, test description, 99.99, 1, test name)'


def test_equality():
    space1 = Space(1, "test description", 99.99, 1, "test name")
    space2 = Space(1, "test description", 99.99, 1, "test name")
    assert space1 == space2
