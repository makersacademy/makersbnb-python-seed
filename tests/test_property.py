from lib.models.property import *
from datetime import datetime
def test_property_init():
<<<<<<< HEAD
    property = Property(1, '123 Main Street', 45, 'This is a house', datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
=======
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
>>>>>>> main
    assert property.id == 1
    assert property.name == '123 Main Street'
    assert property.price == 45
    assert property.description == 'This is a house'
    assert property.available_from == datetime(2024, 1, 1)
    assert property.available_to == datetime(2024, 1, 31)
    assert property.owner_id == 1

def test_property_str_repr():
<<<<<<< HEAD
    property = Property(1, '123 Main Street', 45, 'This is a house', datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert str(property) == 'Property(1, 123 Main Street, 45, This is a house, 2024-01-01 00:00:00, 2024-01-31 00:00:00, 1)'

def test_eq():
    property = Property(1, '123 Main Street', 45, 'This is a house', datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert property == Property(1, '123 Main Street', 45, 'This is a house', datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
=======
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert str(property) == 'Property(1, 123 Main Street,  This is a house, 45, 2024-01-01 00:00:00, 2024-01-31 00:00:00, 1)'

def test_eq():
    property = Property(1, '123 Main Street',  'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
    assert property == Property(1, '123 Main Street', 'This is a house', 45, datetime(2024, 1, 1), datetime(2024, 1, 31), 1)
>>>>>>> main
