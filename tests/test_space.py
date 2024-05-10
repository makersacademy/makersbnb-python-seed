from lib.space import *
"""
Space constructs with an id, name, description, price and user_id 
"""

def test_space_constructs_with_fields():
    space = Space(1, 'Test name', 'Test description', 10, 1)
    assert space.id == 1
    assert space.name == 'Test name'
    assert space.description == 'Test description'
    assert space.price == 10
    assert space.user_id == 1

"""
We can format spaces into a string
"""

def test_space_formats_to_string():
    space = Space(1, 'Test name', 'Test description', 10, 1)
    assert str(space) == "Space(1, Test name, Test description, 10, 1)"


"""
We can compare two identical spaces
and have them be equal
"""

def test_spaces_are_equal():
    space1 = Space(1, 'Test name', 'Test description', 10, 1)
    space2 = Space(1, 'Test name', 'Test description', 10, 1)
    assert space1 == space2