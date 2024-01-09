from lib.space import Space

"""
We are testing the constructor with the specific attributes
"""

def test_space_constructors():
    space = Space(1, "Test Name", "Test Description", 50, '25-12-23', '30-12-23')
    assert space.id == 1
    assert space.name == "Test Name"
    assert space.description == "Test Description"
    assert space.price == 50
    assert space.start_date == '25-12-23'
    assert space.end_date == '30-12-23'
#Testing to compare two identical spaces

def test_identical_spaces():
    space1 = Space(1, "Test Name", "Test Description", 50, '25-12-23', '30-12-23')
    space2 = Space(1, "Test Name", "Test Description", 50, '25-12-23', '30-12-23')
    assert space1 == space2

    