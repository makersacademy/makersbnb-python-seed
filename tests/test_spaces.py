from lib.spaces import *
import datetime

"""
When I create a space,
it should not be a None object,
this shows that space is created.
"""

def test_space_created():
    tempSpace = Space(1, "TestSpace", "test", 1.5, 1)
    assert(type(tempSpace) is not None)

""""
As a user, 
they can create multiple spaces.
"""

def test_multiple_space_created():
    tempSpace1 = Space(1, "testspace1", "test", 1.5, 1)
    tempSpace2 = Space(2, "testspace2", "test", 1.5, 1)
    assert(type(tempSpace1) is not None)
    assert(type(tempSpace2) is not None)

def test_space_validity():
    assert Space(1, "", "", "", []).is_valid() == False

def test_generated_error():
    assert Space(1, "", "test", 1.5, 1).generate_errors() == "Name can't be blank"
    assert Space(1, "TestName", "", 1.5, 1).generate_errors() == "Description can't be blank"
    assert Space(1, "TestName", "test", '', 1).generate_errors() == "Price can't be blank"