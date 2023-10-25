from lib.space import *
from lib.space_repository import *

def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces[:1] == [
        Space('Beach House', 'The most relaxing place', 187, 999, 3, 1)
    ]
    
def test_find_space_with_id(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    album = repository.find(3)
    
    assert album == Space('City Centre House', 'The most popular place', 55, 276, 3)
    

def test_create_space_method(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    space  = Space('New space', 'Very nice space', 140, 899, 2)
    
    id = repository.create(space)
    created_space = repository.find(4)

    assert id['id'] == 4
    assert created_space == space
    
    
def test_delete_space_method(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    
    repository.delete(4)
    deleted_space = repository.find(4)
    spaces = repository.all()
    
    assert deleted_space == None
    assert len(spaces) == 3
    
    
    