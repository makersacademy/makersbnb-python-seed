from lib.space_repository import SpaceRepository
from lib.space import Space


# TO ADD - once all() method is defined

# def test_create_space(db_connection):
#     db_connection.seed('seeds/airbnb.sql')
#     repository = SpaceRepository(db_connection)
#     space = Space(None, "Beach house", "Relaxing place", "210", "80", 1)
    
#     repository.create(space)
#     result = repository.all()

#     assert result == [
#         Space(1, "Beach house", "Relaxing place", 210, 80, 1)
#     ]

# def test_error_message_if_missing_input(db_connection):
#     repository = SpaceRepository(db_connection)
#     space = Space(None, "Beach house", "Relaxing place", "210", "80", 1)
    
#     created_space = repository.create(space)
