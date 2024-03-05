from lib.space import Space

"""
Test constructs with info
"""
def test_construct():
    space = Space(1, "house", 19.99, 'liveable space',1)
    assert space.id == 1
    assert space.name == 'house'
    assert space.price == 19.99
    assert space.description == 'liveable space'
    assert space.user_id == 1

"""
test identical spaces are the same
"""
def test_spaces_are_equal():
    space1 = Space(1, "house", 19.99, 'liveable space',1)
    space2 = Space(1, "house", 19.99, 'liveable space',1)
    assert space1 == space2

"""
test formatting
"""
def test_format():
    space = Space(1, "house", 19.99, 'liveable space',1)
    assert str(space) == "Space(1, house, 19.99, liveable space, 1)"