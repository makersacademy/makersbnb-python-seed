from lib.space import *
from lib.space_repository import *

def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [
        Space(1, 'Beach House', 'The most relaxing place', 187, 999, 3),
        Space(2, 'Lake House', 'The most quiet place', 157, 879, 3),
        Space(3, 'City Centre House', 'The most popular place', 55, 276, 3)
    ]
    
def test_find_space_with_id(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    space = repository.find(3)
    
    assert space == Space(3, 'City Centre House', 'The most popular place', 55, 276, 3)
    

def test_create_space_method(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    space = Space(None, "Beach house", "Relaxing place", "210", "80", 1)
    
    repository.create(space)
    result = repository.all()

    assert result == [
        Space(1, 'Beach House', 'The most relaxing place', 187, 999, 3),
        Space(2, 'Lake House', 'The most quiet place', 157, 879, 3),
        Space(3, 'City Centre House', 'The most popular place', 55, 276, 3),
        Space(4, "Beach house", "Relaxing place", 210, 80, 1)
    ]
    
    
def test_delete_space_method(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    
    repository.delete(4)
    deleted_space = repository.find(4)
    spaces = repository.all()
    
    assert deleted_space == None
    assert len(spaces) == 3
    
    
    