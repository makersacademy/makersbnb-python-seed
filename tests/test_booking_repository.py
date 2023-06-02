from lib.bookings import *
from lib.booking_repository import *

def test_retrieve_all_bookings(db_connection):

    #Seed the test DB with the test data
    db_connection.seed("seeds/makersbnb.sql")

    #Create instance of BookingRepo
    test_booking_repo = BookingRepository(db_connection)

    #Call the currently inactive all function and store in variable
    bookings = test_booking_repo.all()

    #Assert the variable is correctly returned as a list of correct Booking instances
    assert bookings == [

        Booking(1, 1, '2022-01-01', False),
        Booking(2, 2, '2022-02-02', False),
        Booking(3, 1, '2022-03-03', False),

    ]

def test_get_pending_requests(db_connection):

    db_connection.seed("seeds/makersbnb.sql")

    test_booking_repo = BookingRepository(db_connection)

    #Request pending bookings for user id 1 and 2
    user_1_bookings = test_booking_repo.get_all_pending_booking_requests(1)
    user_2_bookings = test_booking_repo.get_all_pending_booking_requests(2)

    #Assert these are the correct bookings returned, and in the correct format
    assert user_1_bookings == [

        Booking(1, 1, '2022-01-01', False),
        Booking(3, 1, '2022-03-03', False),

    ]

    assert user_2_bookings == [

        Booking(2, 2, '2022-02-02', False),

    ]


def create_and_retrieve_booking(db_connection):

    db_connection.seed("seeds/makersbnb.sql")

    test_booking_repo = BookingRepository(db_connection)

    #Firstly, assert the repo is same as usual prior to creating a new booking
    user_1_bookings_before_new = test_booking_repo.get_all_pending_booking_requests(1)

    assert user_1_bookings_before_new == [

        Booking(1, 1, '2022-01-01', False),
        Booking(3, 1, '2022-03-03', False),

    ]

    #Then, create a new booking
    test_booking = Booking(1, 1, 1, '2023-06-01')

    #And add to the repo
    test_booking_repo.create(test_booking)

    #Retrieve bookings again
    user_1_bookings_after_new = test_booking_repo.get_all_pending_booking_requests(1)

    assert user_1_bookings_after_new == [

        Booking(1, 1, '2022-01-01', False),
        Booking(3, 1, '2022-03-03', False),
        Booking(1, 1, 1, '2023-06-01', False)

    ]

    #currently working on this from here