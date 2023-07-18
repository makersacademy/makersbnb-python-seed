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

'''
We can assess a booking for validity
'''
def test_booking_is_valid():
    assert Booking(1, '2023-07-22', '2023-07-22', 1, 1).is_valid() == True
    assert Booking(1, '2023-07-22', '2023-08-24', 1, 1).is_valid() == True
    assert Booking(1, '', '', 1, 1).is_valid() == False
    assert Booking(1, '2023-07-22', '', 1, 1).is_valid() == False
    assert Booking(1, '', '2023-07-22', 1, 1).is_valid() == False
    assert Booking(1, None, None, 1, 1).is_valid() == False
    assert Booking(1, '2023-07-22', None, 1, 1).is_valid() == False
    assert Booking(1, None, '2023-07-22', 1, 1).is_valid() == False
    assert Booking(1, '2023-08-22', '2023-07-22', 1, 1).is_valid() == False
    assert Booking(1, '2024-07-22', '2023-07-22', 1, 1).is_valid() == False
    assert Booking(1, '2023-07-22', '2023-07-20', 1, 1).is_valid() == False

'''
We can generate errors for invalid bookings
'''
def test_boooking_errors():
    assert Booking(1, '2023-07-22', '2023-07-22', 1, 1).generate_errors() == None
    assert Booking(1, '', '', 1, 1).generate_errors() == "Please insert: start date, end date"
    assert Booking(1, '2023-07-22', '', 1, 1).generate_errors() == "Please insert: end date"
    assert Booking(1, '', '2023-07-22', 1, 1).generate_errors() == "Please insert: start date"
    assert Booking(1, None, None, 1, 1).generate_errors() == "Please insert: start date, end date"
    assert Booking(1, '2023-07-22', None, 1, 1).generate_errors() == "Please insert: end date"
    assert Booking(1, None, '2023-07-22', 1, 1).generate_errors() == "Please insert: start date"
    assert Booking(1, '2023-08-22', '2023-07-22', 1, 1).generate_errors() == "Please insert: a start date that is earlier than the end date"
    assert Booking(1, '2024-07-22', '2023-07-22', 1, 1).generate_errors() == "Please insert: a start date that is earlier than the end date"
    assert Booking(1, '2023-07-22', '2023-07-20', 1, 1).generate_errors() == "Please insert: a start date that is earlier than the end date"