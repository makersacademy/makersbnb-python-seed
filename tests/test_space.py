from lib.space import Space

def test_space_construct():
    space = Space(1, 'Test Name', 'Test description', 200, 1, '0000-01-01', '1000-01-01')
    assert space.id == 1
    assert space.space_name == 'Test Name'
    assert space.description == 'Test description'
    assert space.price == 200
    assert space.start_date == '0000-01-01'
    assert space.end_date == '1000-01-01'