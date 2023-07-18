from lib.booking import Booking
from lib.booking_repository import BookingRepository
from datetime import date

"""
When we call BookingRepository#all
we get a list of booking objects reflecting on the seed data
"""
def test_1_get_all_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepository(db_connection)
    bookings = repo.all()
    
    assert len(bookings) == 4
    assert bookings == [
        Booking(1, date(2024, 1, 1), date(2024,1,8), 1, 4),
        Booking(2,date(2024, 2, 14), date(2024, 2,15), 2, 2),
        Booking(3,date(2024,6,7), date(2024,8,7), 3, 1),
        Booking(4,date(2024,1,10), date(2024,1,16), 1, 3)
        ]

'''
When we call BookingRepository#find(id)
we get the 3rd booking object from the db
'''
def test_2_get_single_booking(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepository(db_connection)
    booking = repo.find(3)
    assert booking == Booking(3,date(2024,6,7), date(2024,8,7), 3, 1)

'''
When we call BookingRepository#create(booking)
a new record is created in the db, this record is being returned 
and also reflected when we call BookingRepository#all
'''
def test_3_create_new_booking(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepository(db_connection)
    assert repo.create(Booking(None,'2023-05-30', '2023-09-15',3,2)) == Booking(5,'2023-05-30', '2023-09-15', 3, 2)
    bookings = repo.all()
    assert bookings == [
        Booking(1, date(2024, 1, 1), date(2024,1,8), 1, 4),
        Booking(2,date(2024, 2, 14), date(2024, 2,15), 2, 2),
        Booking(3,date(2024,6,7), date(2024,8,7), 3, 1),
        Booking(4,date(2024,1,10), date(2024,1,16), 1, 3),
        Booking(5,date(2023,5,30), date(2023,9,15), 3, 2)
    ]