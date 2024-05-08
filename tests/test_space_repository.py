from lib.space import *
from lib.space_repository import *

"""
When i call #all on the SpaceRepo
I get all the spaces back in a list
"""

def test_list_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = SpaceRepository(db_connection)
    result = repository.all()
    assert result ==[
        Space(1,'Test Name 1', 'Test Description 1', 10, 1),
        Space(2,'Test Name 2', 'Test Description 2', 50, 2),
        Space(3,'Test Name 3', 'Test Description 3', 30, 2),
        Space(4,'Test Name 4', 'Test Description 4', 10, 1)
    ]

"""
When i call #find on the SpaceRepo
I get the space with the given id
"""  

def test_find_space(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = SpaceRepository(db_connection)
    result = repository.find(1)
    assert result == Space(1,'Test Name 1', 'Test Description 1', 10, 1)

"""
When i call #create on the SpaceRepo
I create a new space in the database
"""

def test_create_space(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = SpaceRepository(db_connection)
    repository.create('Test Name 5', 'Test Description 5', 100, 1)
    result = repository.all()
    assert result == [
        Space(1,'Test Name 1', 'Test Description 1', 10, 1),
        Space(2,'Test Name 2', 'Test Description 2', 50, 2),
        Space(3,'Test Name 3', 'Test Description 3', 30, 2),
        Space(4,'Test Name 4', 'Test Description 4', 10, 1),
        Space(5,'Test Name 5', 'Test Description 5', 100, 1)
    ]

"""
When i call #delete on the SpaceRepo
I delete the space with the given id
"""

def test_delete_space(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = SpaceRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert result == [
        Space(2,'Test Name 2', 'Test Description 2', 50, 2),
        Space(3,'Test Name 3', 'Test Description 3', 30, 2),
        Space(4,'Test Name 4', 'Test Description 4', 10, 1)
    ]

def test_find_space_and_dates(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = SpaceRepository(db_connection)
    result = repository.find_space_and_dates(1)
    assert result == Space(1,'Test Name 1', 'Test Description 1', 10, 1, [
        Date(1, '2024-01-20', True, 1),
        Date(5, '2024-01-24', False, 1)
    ])