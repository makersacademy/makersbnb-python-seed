from lib.space import Space

"""
We are testing the constructor with the specific attributes
"""

def test_space_constructors():
    space = Space(1, "Test Name", "Test Description", 50)
    assert space.id == 1
    assert space.name == "Test Name"
    assert space.description == "Test Description"
    assert space.price == 50

#Testing to compare two identical spaces

def test_identical_spaces():
    space1 = Space(1, "Test Name", "Test Description", 50)
    space2 = Space(1, "Test Name", "Test Description", 50)
    assert space1 == space2

    