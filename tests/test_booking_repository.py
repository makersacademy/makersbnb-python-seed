from lib.booking_repository import *
from lib.booking import *

"""Get all bookings"""

def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    result = repo.all()
    assert result == [
        Booking(1, 1, '01/01/2023', 'approved'), 
        Booking(2, 2, '01/02/2023', 'approved'),
        Booking(3, 3, '01/03/2023', 'requested'),
        Booking(4, 4, '01/04/2023', 'denied')
        ]
    
    
"""find specific booking using udeer_id"""

def test_find_specific_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    result = repo.find(1)
    assert result == Booking(1, 1, '01/01/2023', 'approved')
    
"""make a booking """
    
def test_make_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = BookingRepository(db_connection)
    result = Booking(5, 5, "01/05/2023", "approved")
    new_booking = repo.create(result)
    new_booking = repo.all()
    assert new_booking == [
        Booking(1, 1, '01/01/2023', 'approved'), 
        Booking(2, 2, '01/02/2023', 'approved'),
        Booking(3, 3, '01/03/2023', 'requested'),
        Booking(4, 4, '01/04/2023', 'denied'),
        Booking(5, 5, '01/05/2023', 'approved' )
        ]