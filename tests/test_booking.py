from lib.booking import Booking

"""
Tests class constructs correctly
"""
def test_constructor():
    booking = Booking(1, 2, 3, 'pending')
    assert booking.id == 1
    assert booking.night_id == 2
    assert booking.user_id == 3
    assert booking.status == 'pending'


"""
Tests formatted string
"""
def test_formatted_string():
    booking = Booking(1, 2, 3, 'pending')
    assert str(booking) == 'Booking(1, 2, 3, pending)'

"""
Tests equality
"""
def test_equality():
    booking1 = Booking(1, 2, 3, 'pending')
    booking2 = Booking(1, 2, 3, 'pending')
    assert booking1 == booking2