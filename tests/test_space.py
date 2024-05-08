from lib.space import *

def test_space_eq_valid():
    space1 = Space(1,"Buckingham Palace",'2024-01-01','2024-06-01',1)
    space2 = Space(1,"Buckingham Palace",'2024-01-01','2024-06-01',1)
    assert space1 == space2

def test_space_eq_invalid():
    space1 = Space(1,"Buckingham Palace",'2024-01-01','2024-06-01',1)
    space2 = Space(1,"Buckingham house",'2024-01-01','2024-06-01',2)
    assert space1 != space2

def test_space_repr():
    space1 = Space(1,"Buckingham Palace",'2024-01-01','2024-06-01', 1)
    assert str(space1) == 'Space(1, Buckingham Palace, 2024-01-01, 2024-06-01, 1)'

def test_isvalid_valid():
    space1 = Space(1,"Buckingham Palace",'2024-01-01','2024-06-01', 1)
    assert space1.is_valid() == True

def test_isvalid_notitle():
    space1 = Space(1,"",'2024-01-01','2024-06-01', 1)
    assert space1.is_valid() == False

def test_generateerrors_valid():
    space1 = Space(1,"Buckingham palace",'2024-01-01','2024-06-01', 1)
    assert space1.generate_errors() == None

def test_generateerrors_notitle():
    space1 = Space(1,"",'2024-01-01','2024-06-01', 1)
    assert space1.generate_errors() == "Title can't be blank!"
