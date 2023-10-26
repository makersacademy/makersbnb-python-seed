from uuid import uuid4

from lib.space.space import Space

def test_space_constructs():
    space = Space(1, 'Test Name', 'Test description', 'Test owner_id', 'Test start_date', 'Test end_date')
    assert space.id == 1
    assert space.name == 'Test Name'
    assert space.description == 'Test description'
    assert space.owner_id == 'Test owner_id'
    assert space.start_date == 'Test start_date'
    assert space.end_date == 'Test end_date'
   
    
def test_spaces_are_equal():
    space1 = Space(1, 'Test Name', 'Test description', 'Test owner_id', 'Test start_date', 'Test end_date')
    space2 = Space(1, 'Test Name', 'Test description', 'Test owner_id', 'Test start_date', 'Test end_date')
    assert space1 == space2