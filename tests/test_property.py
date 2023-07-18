from lib.property import Property


# Test for the construction of the property class
def test_property_constructor():
    property = Property(1,"NameTest1","DescriptionTest1",50.00,1)
    assert property.id == 1
    assert property.name == "NameTest1"
    assert property.description == "DescriptionTest1"
    assert property.price == 50.00
    assert property.user_id == 1

# given two same inputs it returns the same output
def test_compare_inputs_for_same_output():
    property = Property(1,"NameTest1","DescriptionTest1",50.00,1)
    property1 = Property(1,"NameTest1","DescriptionTest1",50.00,1)
    assert property == property1

# when given a property object it returns a formatted string output
def test_property_formatted_correctly():
    property = Property(1,"NameTest1","DescriptionTest1",50.00,1)
    assert str(property) == "Property(1,NameTest1,DescriptionTest1,50.00,1)"