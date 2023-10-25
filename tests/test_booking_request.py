from lib.booking_request import *

""" construct user id space id date,and status( requested approved deenied )"""

def test_construct():
    booking_request = BookingRequest(1, 1, "01/01/2023", "approved")
    assert booking_request.user_id == 1
    assert booking_request.space_id == 1 
    assert booking_request.booking_request_date == "01/01/2023"
    assert booking_request.booking_request_status == "approved"
    
""" make booking_request 1 equal to booking_request 2 """

def test_eq():
    booking_request_1 = BookingRequest(1, 1, "01/01/2023", "approved")
    booking_request_2 = BookingRequest(1, 1, "01/01/2023", "approved")
    assert booking_request_1 == booking_request_2
    
    
""" Format the booking_request nicely in a string """

def test_format_string():
    booking_request = BookingRequest(1, 1, "01/01/2023", "approved")
    assert f"{booking_request}" == "1, 1, 01/01/2023, approved"