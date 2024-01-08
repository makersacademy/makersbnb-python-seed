from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date
'''
When we call #all
we get all the bookings back as instances
'''

# def test_all(db_connection):
#     db_connection.seed("seeds/airbnb.sql")
#     repository = BookingRepository(db_connection)
#     result = repository.all() 
#     assert result == [Booking(1, 3, 2, '2024-10-10', '2024-10-12', False), Booking(2, 1, 3, '2024-08-07', '2024-08-15', False), Booking(3, 2, 4, '2024-12-25', '2024-12-31', False)]

def test_create(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = BookingRepository(db_connection)
    booking = Booking(None, 1, 2, '2024-1-22', '2024-3-1', False)
    id = repository.create(booking)
    assert id != None

def test_find_a_specific_booking(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = BookingRepository(db_connection)
    specific_booking = repository.find(2)
    assert specific_booking == Booking(2, 1, 3, date(2024, 8, 7), date(2024, 8, 15), False)

def test_delete_a_booking(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = BookingRepository(db_connection)
    
    bookings = repository.all()
    assert bookings[-1] == Booking(3, 2, 4, date(2024, 12, 25), date(2024, 12, 31), False)
    
    repository.delete(3)
    assert len(repository.all()) == 2

def test_update_a_booking(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = BookingRepository(db_connection)
    
    bookings = repository.all()
    assert bookings[-1] == Booking(3, 2, 4, date(2024, 12, 25), date(2024, 12, 31), False)
    
    repository.update(3, 'confirmed', True)
    
    bookings = repository.all()
    assert bookings[-1] == Booking(3, 2, 4, date(2024, 12, 25), date(2024, 12, 31), True)
