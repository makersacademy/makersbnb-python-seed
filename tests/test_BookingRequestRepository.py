from lib.BookingRequestRepository import BookingRequestRepository
from lib.BookingRequest import BookingRequest
from datetime import date

def test_get_BookingRequests (db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/bedsforbodies_seed.sql")

    myRequests = BookingRequestRepository(db_connection)
    results = myRequests.all()

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 1, 2, 1, 'PENDING'),
        BookingRequest(date(2025,1,1), date(2025,1,8), 2, 3, 2, 'PENDING'),
        BookingRequest(date(2025,2,1), date(2025,2,8), 3, 1, 3, 'PENDING'),
        BookingRequest(date(2025,2,1), date(2025,2,8), 4, 4, 4, 'PENDING')
    ]

def test_create_BookingRequest (db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myBookingRequest = BookingRequest(date(2024,7,8), date(2024,7,9), 1, 2, 0, 'PENDING') # 0 parameter is not needed for the save.
    
    myRequests = BookingRequestRepository(db_connection)    
    myRequests.create(myBookingRequest)
    
    results = myRequests.all()

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 1, 2, 1, 'PENDING'),
        BookingRequest(date(2025,1,1), date(2025,1,8), 2, 3, 2, 'PENDING'),
        BookingRequest(date(2025,2,1), date(2025,2,8), 3, 1, 3, 'PENDING'),
        BookingRequest(date(2025,2,1), date(2025,2,8), 4, 4, 4, 'PENDING'),
        BookingRequest(date(2024,7,8), date(2024,7,9), 1, 2, 5, 'PENDING')
    ]

def test_get_bookings_by_customer(db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    results = myRequests.get_bookings_by_customer(3)

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 2, 3, 2, 'PENDING')
    ]

def test_get_bookings_by_property (db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    results = myRequests.get_bookings_by_property(1)

    assert results == [
        BookingRequest(date(2025,1,1), date(2025,1,8), 1, 2, 1, 'PENDING')
    ]    

def test_get_booking_detail (db_connection):

    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    results = myRequests.get_request_detail(4)

    assert results == BookingRequest(date(2025,2,1), date(2025,2,8), 4, 4, 4, 'PENDING', 'test_property4', 'This place is cool', 'test4')

def test_update_booking_status_approved (db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    # Arrange
    myBooking = myRequests.get_request_detail(4)
    
    # Act

    myBooking.approveRequest()
    myRequests.updateBooking(myBooking)
    
    #Assert

    myBooking = myRequests.get_request_detail(4)
    assert myBooking.status == 'APPROVED'

def test_update_booking_status_rejected (db_connection):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    myRequests = BookingRequestRepository(db_connection)    
    
    # Arrange
    myBooking = myRequests.get_request_detail(1)
    
    # Act

    myBooking.rejectRequest()
    myRequests.updateBooking(myBooking)
    
    #Assert

    myBooking = myRequests.get_request_detail(1)
    assert myBooking.status == 'REJECTED'
