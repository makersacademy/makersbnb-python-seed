from lib.Space import Space


def test_equivilancy():
    space1= Space(1,'Test','Test desc',12.12,'somedates',1) 
    space2= Space(1,'Test','Test desc',12.12,'somedates',1)
    assert space1 == space2
    
    
    