from lib.booking import Booking
from datetime import date

'''
Constructs with id, space_id, booker_id, start_date, end_date, confirmed
'''
def test_constructs_with():
    booking = Booking(1, 3, 2, date(2024,10,10), date(2024, 10, 12), False)
    assert booking.id == 1
    assert booking.space_id == 3
    assert booking.booker_id == 2
    assert booking.start_date == date(2024,10,10)
    assert booking.end_date == date(2024, 10, 12)
    assert booking.confirmed == False

'''
We can have two identical booking and they can be equal
'''
def test_equality():
    booking_1 = Booking(1, 3, 2, date(2024,10,10), date(2024, 10, 12), False)
    booking_2 = Booking(1, 3, 2, date(2024,10,10), date(2024, 10, 12), False)
    assert booking_1 == booking_2

'''
We can format bookings to strings nicely
'''

def test_formatting():
    booking = Booking(1, 3, 2, date(2024, 10, 10), date(2024, 12, 10), True)
    assert str(booking) == "Booking(1, 3, 2, 2024-10-10, 2024-12-10, True)"