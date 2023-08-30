from lib.properties import *

"""
Given an id, id, title, and author name, 
we should be able to instantiate a properties object with those properties 
"""
def test_construct():
    properties = Properties(1, 'Flat', 'Sunny 2bdr flat in city centre', 100, 'Hackney', '2023-08-30', '2023-12-31', '1', 1 )
    assert properties.id == 1 
    assert properties.property_type == "Flat"
    assert properties.description == "Sunny 2bdr flat in city centre"
    assert properties.price == 100
    assert properties.location == "Hackney"
    assert properties.start_date == "2023-08-30"
    assert properties.end_date == "2023-12-31"
    assert properties.available == "1"
    assert properties.user_id == 1

"""
When you construct two propertiess with the same properties, 
they are equal
"""

def test_equal():
    properties_1 = Properties(1, 'Flat', 'Sunny 2bdr flat in city centre', 100, 'Hackney', '2023-08-30', '2023-12-31', '1', 1 )
    properties_2 = Properties(1, 'Flat', 'Sunny 2bdr flat in city centre', 100, 'Hackney', '2023-08-30', '2023-12-31', '1', 1 )
    assert properties_1 == properties_2 


"""
When I construct a properties, 
and I format it to a string, 
it comes out in a nice format 
"""

def test_format(): 
    properties = Properties(1, 'Flat', 'Sunny 2bdr flat in city centre', 100, 'Hackney', '2023-08-30', '2023-12-31', '1', 1 )
    assert str(properties) == '1 - Flat - Sunny 2bdr flat in city centre - 100 - Hackney - 2023-08-30 - 2023-12-31 - 1 - 1'
