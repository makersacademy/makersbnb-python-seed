from lib.space_repository import SpaceRepository
from lib.space import Space 

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)
    
    spaces = repository.all()
    
    assert spaces == [Space(1, 'London', 'city', 200, 1, '2024-02-01', '2025-02-01')]