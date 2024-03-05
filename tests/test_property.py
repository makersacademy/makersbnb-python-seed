from lib.property import *

'''
constructs with an id, property_name , user_id, description, area, price_per_night
'''

def test_constructs():
    property = Property(1, "property1" , 1 , "hot" , 45.5)
    assert property._id == 1
    assert property._property_name == "property1"
    assert property._user_id == 1
    assert property._description == "hot"
    assert property._price_per_night == 45.5

'''
# property can be compared to equality

'''

def test_compares():
    property_1 = Property(1, "property1" , 1 , "hot" , 45.5)
    property_2 = Property(1, "property1" , 1 , "hot" , 45.5)
    assert property_1 == property_2


'''
# property string reprentation is outputed as desired

'''

def test_string_representation():
    property = Property(1, "property1" , 1 , "hot" , 45.5)
    assert str(property) == "Property(1, property1, 1, hot, 45.5)"