from lib.space import *  

def test_creates_space_instance():
    space = Space(1, "Bob House", "Brighton", "3 bedrooms, 2 bathrooms, Victorian-era property", 300, "Bob")
    assert space.id == 1
    assert space.name == "Bob House"
    assert space.location == "Brighton"
    assert space.description == "3 bedrooms, 2 bathrooms, Victorian-era property"
    assert space.price == 300
    assert space.owner == "Bob"

#Test to confirm equality of a record

def test_record_is_equal():
    space_1 = Space('1', 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')
    space_2 = Space('1', 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')
    assert space_1 == space_2

#Tests that Space object is returned in
def test_formats_spaces_records_nicely():
    space = Space('1', 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')
    assert str(space) == 'ID: 1. Property name: Bob House. Location: Brighton. Property Description: 3 bedrooms, 2 bathrooms, Victorian-era property. Price per night: £300. Owner name and contact: Bob.'
