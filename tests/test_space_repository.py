from lib.space_repository import SpaceRepository
from lib.space import Space

def test_create_space(db_connection):
    db_connection.seed('seeds/airbnb.sql')
    repository = SpaceRepository(db_connection)
    space = Space(None, "Beach house", "Relaxing place", "210", "80", 1)
    created_space = repository.create(space)

    assert created_space == Space(1, "Beach house", "Relaxing place", "210", "80", 1)

    result = repository.all()

    assert result == [
        Space(1, "Beach house", "Relaxing place", 210, 80, 1)
    ]

def test_error_message_if_missing_input():
    repository = SpaceRepository()
    space = Space(None, "Beach house", "Relaxing place", "210", "80", 1)
    
    created_space = repository.create(space)
