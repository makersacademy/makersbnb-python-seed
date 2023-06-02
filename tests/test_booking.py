from lib.bookings import *

def test_booking_constructs():
    booking = Booking(1, 1, 1, '2023-06-01', False)
    assert booking.id == 1
    assert booking.requester_id == 1
    assert booking.listing_id == 1
    assert booking.booking_date == '2023-06-01'
    assert booking.approved == False

def test_bookings_format_nicely():
    booking = Booking(1, 1, 1, '2023-06-01', False)
    assert str(booking) == "booking(1, 1, 1, 2023-06-01, False)"

def test_bookings_are_equal():
    booking1 = Booking(1, 1, 1, '2023-06-01', False)
    booking2 = Booking(1, 1, 1, '2023-06-01', False)
    assert booking1 == booking2