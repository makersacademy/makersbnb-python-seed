from lib.property import Property

'''
As a user, I want to have a property with all its details
'''

def test_initializer():
    property = Property('Nice Cottage', 'Nice Cottage', 100, "19/04/24", 'George', False)
    assert property.name == 'Nice Cottage'
    assert property.description == 'Nice Cottage'
    assert property.price == 100
    assert property.date == "19/04/24"
    assert property.owner == 'George' #possibly user_id
    assert property.booked_status  == False
    
def test_equal():
    property = Property('Nice Cottage', 'Nice Cottage', 100, "19/04/24", 'George', False)
    property2 = Property('Nice Cottage', 'Nice Cottage', 100, "19/04/24", 'George', False)
    assert property == property2

def test_format_correctly():
    property = Property('Nice Cottage', 'Nice Cottage', 100, "19/04/24", 'George', False)
    assert str(property) == "Nice Cottage\n Nice Cottage\n £100\n Owner: George"
    
    