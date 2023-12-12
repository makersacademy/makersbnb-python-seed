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