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

"""
When we call BookingRepository#find_by_property_id
it returns a list of booking objects for that property
"""
def test_find_by_property_id(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = BookingRepository(db_connection)
    list_of_bookings = repository.find_by_property_id(3)
    assert list_of_bookings == [
        Booking(3,date(2024,6,7), date(2024,8,7), 3, 1)
    ]

    
"""
When we call BookingRepository#availability_checker
when start date and end date for a given property clash 
with an existing booking for that property
it returns False
"""
def test_booking_availability_returns_false(db_connection): 
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = BookingRepository(db_connection)
    booking1 = Booking(None,date(2024, 1, 10), date(2024, 1,12), 1, 2)
    availability1 = repository.availability_checker(booking1)
    booking2 = Booking(None,date(2024, 2, 13), date(2024, 2,15), 2, 2)
    availability2 = repository.availability_checker(booking2)
    assert availability1 == False
    assert availability2 == False

"""
When we call BookingRepository#availability_checker
when start date and end date for a given property do not clash 
with an existing booking for that property
it returns True
"""

def test_booking_availability_returns_true(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = BookingRepository(db_connection)
    booking = Booking(None,date(2024, 3, 1), date(2024, 3, 4), 2, 2)
    availability = repository.availability_checker(booking)
    assert availability == True

