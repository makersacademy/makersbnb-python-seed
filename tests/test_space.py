from lib.space import Space
import pytest

"""
If we create an instance of Space, it has the attributes
"""
def test_space_model_class():
    space = Space(1, 'Test name', 'Description of space', 20)
    assert space.id == 1
    assert space.name == 'Test name'
    assert space.description == 'Description of space'
    assert space.price == 20

"""
We thought about checking for invalid inputs (i.e. price as a string) here, but
we thought this could be better placed in the form/routes when receiving data from the user
"""
