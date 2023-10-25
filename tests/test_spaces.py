from lib.space_class import Space
from lib.space_repository import SpaceRepository

def test_get_host_requests(db_connection):
    spaces_repo = SpaceRepository(db_connection)
    spaces_repo.get_host_requests(3)