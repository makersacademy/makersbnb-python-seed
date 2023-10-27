from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.database_connection import *

def test_get_all_records(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [
        Space(1, 'The Devonshire Laisure & Spa', 'This is a calm, quiet place where you can completely relax and gain strength', 180, 1),
        Space(2, 'Helmsley Black Swan Appartments', 'this apartment is located in the city centre', 250, 1)
    ]   

