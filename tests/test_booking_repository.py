import pytest
from unittest.mock import Mock
from datetime import date
from lib.booking import Booking
from lib.booking_repository import BookingRepository

def test_booking_repo_init():
    try:
        connection = Mock()
        booking_repo = BookingRepository(connection)
    except Exception as err:
        raise AssertionError(f"An error was raised: {err}")
    
def test_booking_repo_all(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.all() == [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(5, date(2024,2,1), 1, 2, None),
        Booking(6, date(2024,11,22), 3, 1, False)
    ]

def test_booking_repo_find(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    bookings = [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(5, date(2024,2,1), 1, 2, None),
        Booking(6, date(2024,11,22), 3, 1, False)
    ]
    for i in range(len(bookings)):
        assert booking_repo.find(i+1) == bookings[i]

def test_booking_repo_create(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    new_booking = Booking(None, date(2024,1,15), 5, 2, None)
    assert booking_repo.create(new_booking) == None
    
    bad_booking = Booking(None, date(2025,1,1), 3, 1, None)
    with pytest.raises(Exception) as err:
        booking_repo.create(bad_booking)
    assert err.value == "That date is not available!"


@pytest.mark.skip(reason="Test not written")
def test_booking_repo_delete():
    pass

@pytest.mark.skip(reason="Test not written")
def test_booking_repo_update():
    pass