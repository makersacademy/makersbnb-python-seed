from lib.request_repository import *
from datetime import date

def test_add_request(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = RequestRepository(db_connection)
    request = Request(None, 2, date(2024, 2, 2), 2)
    repository.add(request)
    result = repository.all()
    assert request.id == 2
    assert result == [
        Request(1, 1, date(2024, 1, 1), 1, 2),
        Request(2, 2, date(2024, 2, 2), 2, 3)
        ]

def test_get_request(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = RequestRepository(db_connection)
    request = repository.all()
    assert request == [
        Request(1, 1, date(2024, 1, 1), 1, 2)
    ]

def test_get_request_by_id(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = RequestRepository(db_connection)
    request = repository.get_request_by_id(1)
    assert request == Request(1, 1, date(2024, 1, 1), 1, 2)

def test_approve_request(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = RequestRepository(db_connection)
    request_id = 2
    repository.approve_request(request_id)
    approved_request = repository.get_request_by_id(request_id)
    assert approved_request.approved == True



#     pass

# def test_reject_request():
#     pass