from lib.bookings import *

# 
def test_booking_constructs():
    booking = Booking(1, 1, 1, '2023-06-01')
    assert booking.id == 1
    assert booking.user_id == 1
    assert booking.listing_id == 1
    assert booking.booking_date == '2023-06-01'

# """
# We can format bookings to strings nicely
# # """
def test_bookings_format_nicely():
    booking = Booking(1, 1, 1, '2023-06-01')
    assert str(booking) == "booking(1, 1, 1, 2023-06-01)"
#     # Try commenting out the `__repr__` method in lib/booking.py
#     # And see what happens when you run this test again.

# # """
# # We can compare two identical bookings
# # And have them be equal
# # """
def test_bookings_are_equal():
    booking1 = Booking(1, 1, 1, '2023-06-01')
    booking2 = Booking(1, 1, 1, '2023-06-01')
    assert booking1 == booking2