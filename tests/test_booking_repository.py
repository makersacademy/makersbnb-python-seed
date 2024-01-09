from lib.booking import Booking
from lib.booking_repository import BookingRepository


def test_booking_repository_all(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    result = repository.all()
    assert result == [Booking(1, '2024-01-01', False, 1, 1)]


def test_create_booking(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    new_booking = Booking(2, '2024-02-02', False, 1, 1)
    repository.create(new_booking)
    
    result = repository.all()

    assert result == [Booking(1, '2024-01-01', False, 1, 1),
                    Booking(2, '2024-02-02', False, 1, 1)]