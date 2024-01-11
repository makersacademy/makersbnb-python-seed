from lib.RequestRepository import RequestRepository
from lib.Request import Request
from datetime import date

'''
Get all records from Request Repository.
'''

def test_get_all_records(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = RequestRepository(db_connection)
    
    requests = repository.all()

    assert requests == [
        Request(1, 2, date(2024, 1, 12), 'Approved'),
        Request(2, 4, date(2024, 2, 14), 'Denied'),
        Request(3, 5, date(2024, 3, 15), 'Approved'),
    ]
'''
Create a new booking request.
'''

def test_create_booking_request(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = RequestRepository(db_connection)
    
    repository.create(Request(2, 3, date(2024, 6, 13), 'Approved'))
    
    
    result = repository.all()
    assert result == [
        Request(1, 2, date(2024, 1, 12), 'Approved'),
        Request(2, 4, date(2024, 2, 14), 'Denied'),
        Request(3, 5, date(2024, 3, 15), 'Approved'),
        Request(2, 3, date(2024, 6, 13), 'Approved'),
    ]
