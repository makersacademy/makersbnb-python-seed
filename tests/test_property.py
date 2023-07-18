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


# We can assess a propert for validity
def test_book_validity():
    assert Property(1, "", "","","").is_valid() == False

    assert Property(1,None,"","","").is_valid() == False
    assert Property(1,"TestName","","","").is_valid() == False

    assert Property(1,"",None,"","").is_valid() == False
    assert Property(1,"TestName",None,"","").is_valid() == False
    assert Property(1,"TestName","TestDescr","","").is_valid() == False
    
    assert Property(1,"","",None,"").is_valid() == False
    assert Property(1,"TestName","TestDescr",None,"").is_valid() == False
    assert Property(1,"TestName","TestDescr", 50,"").is_valid() == False
    
    assert Property(1,"","", "", None).is_valid() == False
    assert Property(1,"TestName","TestDescr", 50,None).is_valid() == False

    assert Property(1,"TestName","TestDescr", 50,1).is_valid() == True
    assert Property(None,"TestName","TestDescr", 50,1).is_valid() == True


# We can generate errors for an invalid Property
def test_property_errors():
    assert Property(1,"","","","").generate_errors() == "Name can't be blank, Description can't be blank, Price can't be blank, User ID can't be blank"
    
    assert Property(1,None,"","","").generate_errors() == "Name can't be blank, Description can't be blank, Price can't be blank, User ID can't be blank"
    
    assert Property(1,"TestName","","","").generate_errors() == "Description can't be blank, Price can't be blank, User ID can't be blank"
    assert Property(1,"TestName",None,"","").generate_errors() == "Description can't be blank, Price can't be blank, User ID can't be blank"
    
    assert Property(1,"TestName","TestDescr","","").generate_errors() == "Price can't be blank, User ID can't be blank"
    assert Property(1,"TestName","TestDescr",None,"").generate_errors() == "Price can't be blank, User ID can't be blank"
    
    assert Property(1,"TestName","TestDescr",50,"").generate_errors() == "User ID can't be blank"
    assert Property(1,"TestName","TestDescr",50,None).generate_errors() == "User ID can't be blank"
    
    assert Property(1,"TestName","TestDescr", 50,1).generate_errors() == None
    assert Property(None,"TestName","TestDescr", 50,1).generate_errors() == None