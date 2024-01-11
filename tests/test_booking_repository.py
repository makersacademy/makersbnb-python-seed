from lib.booking import Booking
from lib.booking_repository import BookingRepository


def test_booking_repository_all(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    result = repository.all()
    assert result == [Booking(1, '2024-01-01', False, 1, 1),
                    Booking(2, '2024-01-02', False, 1, 2),
                    Booking(3, '2024-01-03', False, 2, 2)]


def test_create_booking(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    new_booking = Booking(4, '2024-02-02', False, 1, 1)
    repository.create(new_booking)
    
    result = repository.all()

    assert result == [Booking(1, '2024-01-01', False, 1, 1),
                    Booking(2, '2024-01-02', False, 1, 2),
                    Booking(3, '2024-01-03', False, 2, 2),
                    Booking(4, '2024-02-02', False, 1, 1)]
    
def test_find(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    result = repository.find(1)
    assert result == Booking(1, '2024-01-01', False, 1, 1)
    
def test_delete(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [Booking(2, '2024-01-02', False, 1, 2),
                    Booking(3, '2024-01-03', False, 2, 2)]

def test_confirm(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    repository.confirm(1)
    assert repository.find(1) == Booking(1, '2024-01-01', True, 1, 1)

def test_find_all_by_user(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    result = repository.find_all_by_user(1)
    assert result == [
        Booking(1, '2024-01-01', False, 1, 1),
        Booking(2, '2024-01-02', False, 1, 2)
    ]

def test_find_all_by_space(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = BookingRepository(db_connection)
    result = repository.find_all_by_space(2)
    assert result == [
        Booking(2, '2024-01-02', False, 1, 2),
        Booking(3, '2024-01-03', False, 2, 2)
    ]