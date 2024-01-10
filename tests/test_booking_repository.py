from lib.booking_repository import *


def test_find_single_user(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    user = repository.find(1)
    assert user == [
        Booking(1, 1, 3,'2024-02-01', 'Celestial Haven'),
        Booking(2, 1, 2, '2024-04-10', 'Zootropolis'),
    ]

    
def test_create_booking(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    booking = Booking(None, 1, 1, '2022-01-01', 'Devon')
    repository.create(booking)
    user = repository.find(1)
    assert user == [
        Booking(1, 1, 3,'2024-02-01', 'Celestial Haven'),
        Booking(2, 1, 2, '2024-04-10', 'Zootropolis'),
        Booking(8, 1, 1, '2022-01-01', 'Devon')
    ]







