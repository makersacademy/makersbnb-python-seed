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
        Request(1, 1, date(2024, 1, 1), 1),
        Request(2, 2, date(2024, 2, 2), 2)
        ]

def test_get_request(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = RequestRepository(db_connection)
    request = repository.all()
    assert request == [
        Request(1, 1, date(2024, 1, 1), 1)
    ]
# def test_approve_request():

#     pass

# def test_reject_request():
#     pass