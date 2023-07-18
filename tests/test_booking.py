from lib.booking import Booking

'''
booking constructs with an id, title  and author_name
'''
def test_booking_constructs():
    booking = Booking(1, '2023-07-22', '2023-07-22', 1, 1)
    assert booking.id == 1
    assert booking.start_date == '2023-07-22'
    assert booking.end_date == '2023-07-22'
    assert booking.property_id == 1
    assert booking.user_id == 1

'''
We can format bookings nicely
'''
def test_booking_formats_nicely():
    booking = Booking(1, '2023-07-22', '2023-07-22', 1, 1)
    assert str(booking) == "Booking(1, 2023-07-22, 2023-07-22, 1, 1)"

'''
We can compare 2 identical bookings
'''
def test_bookings_are_equal():
    booking1 = Booking(1, '2023-07-22', '2023-07-22', 1, 1)
    booking2 = Booking(1, '2023-07-22', '2023-07-22', 1, 1)
    assert booking1 == booking2