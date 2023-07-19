from lib.request_repository import RequestRepository
from lib.request import Request

def test_all(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = RequestRepository(db_connection)
    assert repository.all() == []