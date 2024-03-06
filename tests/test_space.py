from lib.space import Space

"""
Space constructs with an id, name, description, price_per_night, user_id
"""
def test_space_constructs():
    space = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1)
    assert space.id == 1
    assert space.name == 'Cozy Cottage'
    assert space.description == 'A charming cottage in the countryside.'
    assert space.price_per_night == 120.00
    assert space.user_id == 1

"""
We can format spaces to strings nicely
"""
def test_spaces_format_nicely():
    space = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1)
    assert str(space) == "Space(1, Cozy Cottage, A charming cottage in the countryside., 120.00, 1)"

"""
We can compare two identical bookings
And have them be equal
"""
def test_spaces_are_equal():
    space1 = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1)
    space2 = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1)
    assert space1 == space2