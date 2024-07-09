from lib.BookingRequestRepository import BookingRequestRepository
from lib.BookingRequest import BookingRequest
from datetime import date

def test_get_BookingRequests (db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/bedsforbodies_seed.sql")

    myRequests = BookingRequestRepository(db_connection)
    results = myRequests.all()

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 1, 2),
        BookingRequest(date(2025,1,1), date(2025,1,8), 2, 3),
        BookingRequest(date(2025,2,1), date(2025,2,8), 3, 1),
        BookingRequest(date(2025,2,1), date(2025,2,8), 5, 4)
    ]


def test_create_BookingRequest (db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myBookingRequest = BookingRequest(date(2024,7,8), date(2024,7,10), 1, 2)
    
    myRequests = BookingRequestRepository(db_connection)    
    myRequests.create(myBookingRequest)
    
    results = myRequests.all()

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 1, 2),
        BookingRequest(date(2025,1,1), date(2025,1,8), 2, 3),
        BookingRequest(date(2025,2,1), date(2025,2,8), 3, 1),
        BookingRequest(date(2025,2,1), date(2025,2,8), 5, 4),
        BookingRequest(date(2024,7,8), date(2024,7,10), 1, 2)
    ]

def test_get_bookings_by_customer (db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    results = myRequests.get_bookings_by_customer(3)

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 2, 3)
    ]


def test_get_bookings_by_property (db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    results = myRequests.get_bookings_by_property(1)

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 1, 2)
    ]    