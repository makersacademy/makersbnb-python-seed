from lib.booking import Booking

# testing Booking constructor for id, date, confirmed, user_id, space_id
def test_booking():
    booking = Booking(1, "2024-01-01", False, 1, 1)
    assert booking.id == 1
    assert booking.date == '2024-01-01'
    assert booking.confirmed == False
    assert booking.user_id == 1
    assert booking.space_id == 1

def test_booking_formats_nicely():
    booking = Booking(1, "2024-01-01", False, 1, 1)
    assert str(booking) == 'Booking(1, 2024-01-01, False, 1, 1)'

def test_bookings_are_equal():
    booking_1 = Booking(1, "2024-01-01", False, 1, 1)
    booking_2 = Booking(1, "2024-01-01", False, 1, 1)
    assert booking_1 == booking_2