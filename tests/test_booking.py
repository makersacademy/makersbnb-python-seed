from lib.booking import * 

def test_booking_initialises():
    booking = Booking(1, 1, '01/01/2024')
    assert booking.id == 1
    assert booking.user_id == 1
    assert booking.date_booked == '01/01/2024'

def test_repr():
    booking = Booking(1, 1, '01/01/2024')
    assert str(booking) == 'Booking(1, 1, 01/01/2024)'

def test_eq():
    booking_1 = Booking(1, 1, '01/01/2024')
    booking_2 = Booking(1, 1, '01/01/2024')
    assert booking_1 == booking_2