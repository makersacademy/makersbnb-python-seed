import pytest
from lib.booking import Booking

def test_init():
    """ID, Date, Space_ID, Guest_ID, Confirmed"""
    booking = Booking(1, "2024-01-01", 2, 3, True)
    assert booking.id == 1
    assert booking.space_id == 2
    assert booking.guest_id == 3
    assert booking.date == "2024-01-01"
    assert booking.confirmed == True

def test_repr():
    booking = Booking(1, "2024-01-01", 2, 3, True)
    assert str(booking) == "Booking(1, 2024-01-01, 2, 3, True)"

def test_eq():
    booking1 = Booking(1, "2024-01-01", 2, 3, True)
    booking2 = Booking(1, "2024-01-01", 2, 3, True)
    assert booking1 == booking2
