import pytest
from lib.space import Space 

def test_constructs():
    space = Space(1, 'title', 'description', 'price', 'date_range', 1)
    assert space.id == 1
    assert space.title == 'title'
    assert space.description == 'description'
    assert space.price == 'price'
    assert space.date_range == 'date_range'
    assert space.user_id == 1

def test_spaces_are_equal():
    space1 = Space(1, 'title', 'description', 'price', 'date_range', 1)
    space2 = Space(1, 'title', 'description', 'price', 'date_range', 1)
    assert space1 == space2


def test_posts_format_nicely():
    space = Space(1, 'title', 'description', 'price', 'date_range', 1)
    assert str(space) == "Space(1, title, description, price, date_range, 1)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.
