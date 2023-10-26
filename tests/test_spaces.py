from lib.space_class import Space
from lib.space_repository import SpaceRepository

def test_change_status(db_connection):
    db_connection.seed('seeds/MAKERSBNB.sql')
    space_repo = SpaceRepository(db_connection)
    print(space_repo.find_by_id(1))
    space_repo.change_status('approved', 1, '2021-02-24')

def test_change_status_2(db_connection):
    db_connection.seed('seeds/MAKERSBNB.sql')
    space_repo = SpaceRepository(db_connection)
    print(space_repo.find_by_id(1))
    space_repo.change_status('pending', 1, '2021-02-24')
    