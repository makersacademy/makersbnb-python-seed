from lib.space import Space

"""
Space constructs with an id, name, location, price, size, description
"""
def test_space_constructs():
    space = Space(1, "Test name", "London", 100, 2, "Description")
    assert space.name == "Test name"
    assert space.location == "London"
    assert space.price == 100
    assert space.size == 2
    assert space.description == "Description" 
    assert space.id == 1

"""
We can format spaces to strings nicely
"""
def test_space_formats_nicely():
    space = Space(1, "Test name", "London", 100, 2, "Description")
    assert str(space) == "Space(1, Test name, London, 100, 2, Description)"

"""
We can compare two identical spaces
And have them be equal
"""
def test_spaces_are_equal():
    space2 = Space(1, "Test name", "London", 100, 2, "Description")
    space1 = Space(1, "Test name", "London", 100, 2, "Description")
    assert space1 == space2