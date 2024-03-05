from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.utilities import string_to_date

"""
When we call BookingRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/bnb_table.sql") # Seed our database with some test data
    repository = BookingRepository(db_connection) # Create a new BookRepository

    bookings = repository.all() # Get all books

    # Assert on the results
    assert bookings == [
        Booking(1, string_to_date('2024-07-13'), True, 1, 2),
        Booking(2, string_to_date('2024-06-25'), False, 2, 1)
    ]

"""
When we call BookingRepository#find
We get a single Booking object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = BookingRepository(db_connection)

    booking = repository.find(2)
    assert booking == Booking(2, string_to_date('2024-06-25'), False, 2, 1)

"""
When we call BookingRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = BookingRepository(db_connection)

    repository.create(Booking(None, "2024-09-10", False, 1, 2))

    result = repository.all()
    assert result == [
        Booking(1, string_to_date('2024-07-13'), True, 1, 2),
        Booking(2, string_to_date('2024-06-25'), False, 2, 1),
        Booking(3, string_to_date('2024-09-10'), False, 1, 2)
    ]

# """
# When we call BookingRepository#delete
# We remove a record from the database.
# """
def test_delete_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = BookingRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        Booking(2, string_to_date('2024-06-25'), False, 2, 1)
    ]