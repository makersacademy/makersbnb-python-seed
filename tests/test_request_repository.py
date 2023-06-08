from lib.request import Request
from lib.request_repository import RequestRepository
"""
test the function that gives us all requests of one owner
"""
def test_get_all_requests_by_owner(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    request_repository = RequestRepository(db_connection)
    requests = request_repository.get_requests_by_owner_id(1)
    assert requests == [Request(1, 1, 2, 1, '2023-01-08', False)]

"""
test the function that gives us all requests made by the user
"""
def test_get_all_requests_made_by_visitor(db_connection):
    db_connection.seed('seeds/users_spaces.sql')
    request_repository = RequestRepository(db_connection)
    requests = request_repository.get_requests_by_visitor_id(2)
    assert requests == [Request(1, 1, 2, 1, '2023-01-08', False)]
