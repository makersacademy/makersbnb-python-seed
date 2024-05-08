from lib.booking import Booking
from lib.booking_repository import BookingRepository


def test_list_all_bookings(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = BookingRepository(db_connection)
    
    bookings = repository.all()
    
    assert bookings == [
        Booking(1, 1, 4),
        Booking(2, 4, 3),
        Booking(3, 5, 2),
        Booking(4, 5, 5)
    ]
    
    
def test_create_booking(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = BookingRepository(db_connection)

    repository.create(Booking(5, 6, 4))

    booking = repository.all()
    assert booking == [
        Booking(1, 1, 4),
        Booking(2, 4, 3),
        Booking(3, 5, 2),
        Booking(4, 5, 5),
        Booking(5, 6, 4)
    ]
    
    
def test_find_single_booking(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = BookingRepository(db_connection)

    booking = repository.find(3)
    assert booking == Booking(3, 5, 2)
    
    
def test_delete_booking(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = BookingRepository(db_connection)
    repository.delete(3) 

    booking = repository.all()
    assert booking == [
        Booking(1, 1, 4),
        Booking(2, 4, 3),
        Booking(4, 5, 5),
        Booking(5, 6, 4)
    ]
