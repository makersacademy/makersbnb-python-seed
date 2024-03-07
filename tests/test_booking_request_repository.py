from lib.booking_request import BookingRequest
from lib.booking_request_repository import BookingRequestRepository

"""
When we call BookingRepository#all
We get a list of Booking_request objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/bnb_table.sql") # Seed our database with some test data
    repository = BookingRequestRepository(db_connection) # Create a new BookingRequestRepository

    booking_requests = repository.all() # Get all booking request

    # Assert on the results
    assert booking_requests== [
        BookingRequest(1, 1, 'pending'),
        BookingRequest(2, 2, 'confirmed'),
    ]

"""
When we call BookingRequestRepository#find
We get a single BookingRequest object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = BookingRequestRepository(db_connection)

    booking_requests = repository.find(2)
    assert booking_requests == BookingRequest(2, 2,'confirmed')

"""
When we call BookingRequestRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = BookingRequestRepository(db_connection)

    repository.create(BookingRequest(1, 1, 'declined'))

    result = repository.all()
    assert result == [
        BookingRequest(1, 1, 'pending'),
        BookingRequest(2, 2, 'confirmed'),
        BookingRequest(3, 1, 'declined')
    ]

# """
# When we call BookingRequestRepository#delete
# We remove a record from the database.
# """
def test_delete_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = BookingRequestRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        BookingRequest(2, 2, 'confirmed'),

    ]