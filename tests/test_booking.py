from lib.booking import *

""" construct user id space id date,and status( requested approved deenied )"""

def test_construct():
    booking = Booking(1, 1, "01/01/2023", "approved")
    assert booking.user_id == 1
    assert booking.space_id == 1 
    assert booking.booking_date == "01/01/2023"
    assert booking.booking_status == "approved"
    
""" make booking 1 equal to booking 2 """

def test_eq():
    booking_1 = Booking(1, 1, "01/01/2023", "approved")
    booking_2 = Booking(1, 1, "01/01/2023", "approved")
    assert booking_1 == booking_2
    
    
""" Format the booking nicely in a string """

def test_format_string():
    booking = Booking(1, 1, "01/01/2023", "approved")
    assert f"{booking}" == "1, 1, 01/01/2023, approved"