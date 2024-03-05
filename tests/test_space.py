from lib.space import *
from datetime import date


def test_construct():
    space = Space(1, "test description", 99.99, 1, "test name", 2024-1-1, 2024-1-31)
    assert space.id == 1
    assert space.description == "test description"
    assert space.price == 99.99
    assert space.user_id == 1
    assert space.name == "test name"
    assert space.fromdate == 2024-1-1
    assert space.todate == 2024-1-31

def test_format():
    space = Space(1, "test description", 99.99, 1, "test name", date(2024, 1, 1), date(2024, 1, 31))
    assert str(space) == 'Space(1, test description, 99.99, 1, test name, 2024-01-01, 2024-01-31)'


def test_equality():
    space1 = Space(1, "test description", 99.99, 1, "test name", date(2024, 1, 1), date(2024, 1, 1))
    space2 = Space(1, "test description", 99.99, 1, "test name", date(2024, 1, 1), date(2024, 1, 1))
    assert space1 == space2
