from lib.booking_request_repository import *
from lib.booking_request import *

"""Get all booking_requests"""

def test_get_all_booking_requests(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingRequestRepository(db_connection)
    result = repo.all()
    assert result == [
        BookingRequest(1, 1, '01/01/2023', 'approved'), 
        BookingRequest(2, 2, '01/02/2023', 'approved'),
        BookingRequest(3, 3, '01/03/2023', 'requested'),
        BookingRequest(4, 4, '01/04/2023', 'denied')
        ]
    
    
"""find specific booking_request using udeer_id"""

def test_find_specific_booking_request(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingRequestRepository(db_connection)
    result = repo.find(1)
    assert result == BookingRequest(1, 1, '01/01/2023', 'approved')
    
"""make a booking_request """
    
def test_make_booking_request(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingRequestRepository(db_connection)
    result = BookingRequest(5, 5, "01/05/2023", "approved")
    new_booking_request = repo.create(result)
    new_booking_request = repo.all()
    assert new_booking_request == [
        BookingRequest(1, 1, '01/01/2023', 'approved'), 
        BookingRequest(2, 2, '01/02/2023', 'approved'),
        BookingRequest(3, 3, '01/03/2023', 'requested'),
        BookingRequest(4, 4, '01/04/2023', 'denied'),
        BookingRequest(5, 5, '01/05/2023', 'approved' )
        ]