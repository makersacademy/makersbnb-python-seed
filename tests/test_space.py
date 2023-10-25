from lib.space import Space

def test_construct():
    space = Space('test space', 'this is a test', 97, 1200, 1)
    assert space.name == 'test space'
    assert space.size ==  97
    
def test_comparsion():
    space1 = Space('test space', 'this is a test', 97, 1200, 1)
    space2 = Space('test space', 'this is a test', 97, 1200, 1)
    assert space1 == space2
    
def test_formatting():
    space = Space('test space', 'this is a test', 97, 1200, 1)
    assert str(space) == 'Space(test space, this is a test, 97, 1200)'