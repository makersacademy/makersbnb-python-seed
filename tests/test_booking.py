from lib.booking import Booking

def test_booking():
    booking = Booking(1, 1, 4)
    assert booking.id == 1
    assert booking.date_id == 1
    assert booking.user_id == 4
    
def test_equality():
    booking1 = Booking(1, 1, 4)
    booking2 = Booking(1, 1, 4)
    
    assert booking1 == booking2
    
def test_formats_to_string():
    booking = Booking(1, 1, 4)
    assert str(booking) == "Booking(1, 1, 4)"
