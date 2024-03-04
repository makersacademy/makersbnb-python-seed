from lib.space import Space

"""
Constructs with a id, name, description, price and user_id
"""

def test_constructs():
    space = Space(1, "mybnb", "in beverley hills", 9000, 2)
    assert space.id == 1
    assert space.name == "mybnb"
    assert space.description == "in beverley hills"
    assert space.price == 9000
    assert space.user_id == 2


"""
Space with equal contents are equal
"""

def test_equal():
    space1 = Space(1, "mybnb", "in beverley hills", 9000, 2)
    space2 = Space(1, "mybnb", "in beverley hills", 9000, 2)
    assert space1 == space2


"""
Spaces format to string
"""

def test_format():
    space = Space(1, "mybnb", "in beverley hills", 9000, 2)
    assert str(space) == "Space(1, mybnb, in beverley hills, 9000, 2)"