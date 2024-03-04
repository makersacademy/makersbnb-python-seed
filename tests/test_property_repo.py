from lib.property_repo import PropertyRepository
from lib.property import Property
import pytest 

def test_init_connection(db_connection): 
    repo = PropertyRepository(db_connection)
    assert repo._connection == db_connection

def test_all(db_connection):
    db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    repo = PropertyRepository(db_connection)
    properties = repo.all()
    assert properties == [Property(1, 'Chestnut Eco Lodge Woodland Escape', 'House with garden', 101, 1, False),
                        Property(2, 'The Hazel Hide', 'Luxury Eco A-Frame Cabin', 240, 3, False),
                        Property(3, "Entire Contemporary Barn", "Barn in Essex", 550, 5, False), 
                        Property(4, "Coloc All Included Febvotte-Marat", "Room in Tours", 463, 1, False),
                        Property(5, "2RJ2- Hyper center.", "Entire rental unit in Tours", 472, 4, True)
                        ] 
    

def test_find(db_connection):
    # db_connection.seed('seeds/Users.sql')
    db_connection.seed('seeds/properties.sql')
    repo = PropertyRepository(db_connection)
    property = repo.find(1)
    assert property == Property(1, 'Chestnut Eco Lodge Woodland Escape', 'House with garden', 101, 1, False)

