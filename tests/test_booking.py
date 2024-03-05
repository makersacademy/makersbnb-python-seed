from lib.booking import Booking

"""
Booking constructs with an id, date, status, space_id, guest_id
"""
def test_booking_constructs():
    booking = Booking(1, '2024-07-13', True, 1, 2)
    assert booking.id == 1
    assert booking.date == '2024-07-13'
    assert booking.status == True
    assert booking.space_id == 1
    assert booking.guest_id == 2

"""
We can format bookings to strings nicely
"""
def test_bookings_format_nicely():
    booking = Booking(1, '2024-07-13', True, 1, 2)
    assert str(booking) == "Booking(1, 2024-07-13, True, 1, 2)"

"""
We can compare two identical bookings
And have them be equal
"""
def test_books_are_equal():
    booking1 = Booking(1, '2024-07-13', True, 1, 2)
    booking2 = Booking(1, '2024-07-13', True, 1, 2)
    assert booking1 == booking2
    # Try commenting out the `__eq__` method in lib/book.py
    # And see what happens when you run this test again.