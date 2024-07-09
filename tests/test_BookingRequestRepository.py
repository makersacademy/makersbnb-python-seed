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
        BookingRequest(date(2025,2,1), date(2025,2,8), 4, 4)
    ]

