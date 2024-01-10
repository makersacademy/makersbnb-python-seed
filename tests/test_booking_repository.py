from lib.booking import Booking
from lib.booking_repository import BookingRepository


"""
When we call #all
We get a list of all bookings
"""
def test_all_bookings(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    assert booking_repository.all() == [
        Booking(1 ,1, 2, 'pending'),
        Booking(2 ,1, 3, 'pending'),
        Booking(3 ,3, 2, 'confirmed'),
        Booking(4 ,3, 3, 'declined'),
        Booking(5 ,4, 1, 'confirmed'),
        Booking(6 ,5, 2, 'confirmed')
    ]

"""
When we call #find with a booking id
We get the relevant booking returned
"""
def test_find_booking(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    booking = booking_repository.find(2)
    assert booking == Booking(2 ,1, 3, 'pending')

"""
When we call #create with a booking
It gets added to the database
This is reflected when we call #all
"""
def test_create_booking(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    booking_repository.create(Booking(None, 2, 3, 'pending'))
    assert booking_repository.all() == [
        Booking(1 ,1, 2, 'pending'),
        Booking(2 ,1, 3, 'pending'),
        Booking(3 ,3, 2, 'confirmed'),
        Booking(4 ,3, 3, 'declined'),
        Booking(5 ,4, 1, 'confirmed'),
        Booking(6 ,5, 2, 'confirmed'),
        Booking(7, 2, 3, 'pending')
    ]
