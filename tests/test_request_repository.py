from lib.request_repository import RequestRepository
from lib.request import Request
from lib.space_repository import SpaceRepository
from lib.space import Space

def test_all(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = RequestRepository(db_connection)
    assert repository.all() == [Request(1, 1, 1, "01/01/2023", "TBC")]

"""
When we choose avaliable date,
we create a request to book a space
"""
def test_create_request(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = RequestRepository(db_connection)
    repository.create(Request(None, 2, 1, "01/01/2023", "TBC"))
    result = repository.all()
    assert result == [Request(1, 1, 1, "01/01/2023", "TBC"), Request(2, 2, 1, "01/01/2023", "TBC")]

def test_find_request(db_connection):
    repository = RequestRepository(db_connection)
    repository.create(Request(None, 1, 1, "01/01/2023", "TBC"))
    assert repository.find(1) == Request(1, 1, 1, "01/01/2023", "TBC")

def test_confirm_a_request(db_connection):
    repository = RequestRepository(db_connection)
    request = Request(None, 1, 1, "01/01/2023", "TBC")
    repository.create(request)
    request_1 = repository.find(1)
    repository.confirm_booking(request_1)
    assert request_1.request_status == "True"

def test_decline_a_request(db_connection):
    repository = RequestRepository(db_connection)
    request = Request(None, 1, 1, "01/01/2023", "TBC")
    repository.create(request)
    request_1 = repository.find(1)
    repository.decline_a_request(request_1)
    assert request_1.request_status == "False"