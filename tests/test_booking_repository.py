import pytest
from unittest.mock import Mock
from datetime import date
from lib.booking import Booking
from lib.booking_repository import BookingRepository

def test_booking_repo_init():
    """
    Tests that an instantiation of the 
    BookingRepository class raises no errors
    """
    try:
        connection = Mock()
        booking_repo = BookingRepository(connection)
    except Exception as err:
        raise AssertionError(f"An error was raised: {err}")
    
def test_booking_repo_all(db_connection):
    """
    Tests that the #all method returns every booking in the bookings table
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.all() == [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(5, date(2024,2,1), 1, 2, None),
        Booking(6, date(2024,11,22), 3, 1, False)
    ]

def test_booking_repo_find(db_connection):
    """
    Tests that the #find method returns the booking with id == id
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    bookings = [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(5, date(2024,2,1), 1, 2, None),
        Booking(6, date(2024,11,22), 3, 1, False)
    ]
    for i in range(len(bookings)):
        assert booking_repo.find(i+1) == bookings[i]
    
    with pytest.raises(Exception) as err:
        booking_repo.find(7)
    assert str(err.value) == "Booking does not exist."

def test_booking_repo_find_by_guest_id(db_connection):
    """
    Tests that all bookings made by the same user can be retrieved
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.find_by_guest_id(3) == [
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True)
    ]

    with pytest.raises(Exception) as err:
        booking_repo.find_by_guest_id(12)
    assert str(err.value) == "Bookings for this user do not exist."

def test_booking_repo_find_by_space_id(db_connection):
    """
    Tests that all bookings made for the same space can be retrieved
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.find_by_space_id(3) == [
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(6, date(2024,11,22), 3, 1, False)
    ]

    with pytest.raises(Exception) as err:
        booking_repo.find_by_space_id(12)
    assert str(err.value) == "Bookings for this space do not exist."

def test_booking_repo_create(db_connection):
    """
    Tests that a new booking is inserted into the database
    by the #create method
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    new_booking = Booking(None, date(2024,1,15), 5, 2, None)
    assert booking_repo.create(new_booking) == None

    bad_booking = Booking(None, date(2025,1,1), 3, 1, None)
    with pytest.raises(Exception) as err:
        booking_repo.create(bad_booking)
    assert str(err.value) == "That date is not available!"

def test_booking_repo_delete(db_connection):
    """
    Tests that the #delete method removes the booking with id == id
    from the bookings table
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.delete(6) == None
    bookings = [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(5, date(2024,2,1), 1, 2, None)
    ]
    assert booking_repo.all() == bookings
    
    with pytest.raises(Exception) as err:
        booking_repo.delete(7)
    assert str(err.value) == "Booking does not exist."

def test_booking_repo_update(db_connection):
    """
    Tests that the #update method can be used to adjust the values for
    a single booking record in the bookings table
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    updated_booking = Booking(5, date(2024,12,10), 3, 1, None)
    assert booking_repo.update(updated_booking) == None
    assert booking_repo.all() == [
        Booking(1, date(2024,2,1), 1, 2, None),
        Booking(2, date(2024,2,1), 2, 2, None),
        Booking(3, date(2024,11,21), 3, 3, True),
        Booking(4, date(2024,11,22), 3, 3, True),
        Booking(6, date(2024,11,22), 3, 1, False),
        Booking(5, date(2024,12,10), 3, 1, None)
    ]

    bad_update = Booking(None, date(2024,4,1), 4, 1, None)
    with pytest.raises(Exception) as err:
        booking_repo.update(bad_update)
    assert str(err.value) == "Booking does not exist."

def test_booking_repo_confirm(db_connection):
    """
    Tests that the #confirm method sets the confirmed field to True for
    the Booking with id == id
    Also tests that the date is then removed from the dates table
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    date_rows = db_connection.execute(
        """
        SELECT * FROM dates WHERE date=%s AND space_id=%s;
        """, ['2024-02-01', 1]
    )
    assert len(date_rows) == 1
    assert booking_repo.confirm(1)
    assert booking_repo.find(1).confirmed == True
    date_rows = db_connection.execute(
        """
        SELECT * FROM dates WHERE date=%s AND space_id=%s;
        """, ['2024-02-01', 1]
    )
    assert len(date_rows) == 0

def test_booking_repo_reject(db_connection):
    """
    Tests that the #reject method sets the confirmed field to False for
    the Booking with id == id
    """
    db_connection.seed("seeds/makersbnb.sql")
    booking_repo = BookingRepository(db_connection)
    assert booking_repo.reject(1)
    assert booking_repo.find(1).confirmed == False