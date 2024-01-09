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
    
    with pytest.raises(Exception) as err:
        booking_repo.find(7)
    assert str(err.value) == "Booking does not exist."

def test_booking_repo_create(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    new_booking = Booking(None, date(2024,1,15), 5, 2, None)
    assert booking_repo.create(new_booking) == None

    bad_booking = Booking(None, date(2025,1,1), 3, 1, None)
    with pytest.raises(Exception) as err:
        booking_repo.create(bad_booking)
    assert str(err.value) == "That date is not available!"

def test_booking_repo_delete(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.delete(6) == None
    bookings = [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(5, date(2024,2,1), 1, 2, None)
    ]
    assert booking_repo.all() == bookings
    
    with pytest.raises(Exception) as err:
        booking_repo.delete(7)
    assert str(err.value) == "Booking does not exist."

def test_booking_repo_update(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    updated_booking = Booking(5, date(2024,12,10), 3, 1, None)
    assert booking_repo.update(updated_booking) == None
    assert booking_repo.all() == [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(6, date(2024,11,22), 3, 1, False),
        Booking(5, date(2024,12,10), 3, 1, None)
    ]

    bad_update = Booking(None, date(2024,4,1), 4, 1, None)
    with pytest.raises(Exception) as err:
        booking_repo.update(bad_update)
    assert str(err.value) == "Booking does not exist."