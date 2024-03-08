from lib.booking import Booking

"""
Test constructs with info
"""
def test_construct():
    booking = Booking(1, "2024-02-23", "2024-02-24", 2, True, False, 1)
    assert booking.id == 1
    assert booking.booking_start_date == "2024-02-23"
    assert booking.booking_end_date == "2024-02-24"
    assert booking.bookers_id == 2
    assert booking.request_outstanding == True
    assert booking.booked == False
    assert booking.space_id == 1

"""
test identical spaces are the same
"""
def test_spaces_are_equal():
    booking1 = Booking(1, "2024-02-23", "2024-02-24", 2, True, False, 1)
    booking2 = Booking(1, "2024-02-23", "2024-02-24", 2, True, False, 1)
    assert booking1 == booking2

"""
test formatting
"""
def test_format():
    booking = Booking(1, "2024-02-23", "2024-02-24", 2, True, False, 1)
    assert str(booking) == "Booking(1, 2024-02-23, 2024-02-24, 2, True, False, 1)"