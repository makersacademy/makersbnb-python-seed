from lib.space import Space

"""
Test class constructs correctly
"""
def test_constructor():
    space = Space(1, 2, 'House 1', '4 bedroom detatched house.', 110)
    assert space.id == 1
    assert space.user_id == 2
    assert space.name == 'House 1'
    assert space.description == '4 bedroom detatched house.'
    assert space.price_per_night == 110

"""
Tests class equality
"""
def test_equality():
    space1 = Space(1, 2, 'House 1', '4 bedroom detatched house.', 110)
    space2 = Space(1, 2, 'House 1', '4 bedroom detatched house.', 110)
    assert space1 == space2
"""
Test class string format
"""
def test_string_format():
    space = Space(1, 2, 'House 1', '4 bedroom detatched house.', 110)
    assert str(space) == 'Space(1, 2, House 1, 4 bedroom detatched house., 110)'