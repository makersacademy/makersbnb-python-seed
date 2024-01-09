from lib.booking_repository import *


def test_find_single_user(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    
    user = repository.find(1)
    
    assert user == [
        Booking(1, 1, 3,'2024-02-01'),
        Booking(2, 1, 2, '2024-04-10'),
    ]
    
def test_create_booking(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    
    booking = Booking(None, 1, 1, '2022-01-01')
    repository.create(booking)
    user = repository.find(1)
    
    assert user == [
        Booking(1, 1, 3,'2024-02-01'),
        Booking(2, 1, 2, '2024-04-10'),
        Booking(8, 1, 1, '2022-01-01')
    ]