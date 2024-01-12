from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.availability_repository import AvailabilityRepository
from lib.availability import Availability
from lib.space_repository import SpaceRepository
from lib.space import Space
from datetime import date

"""
When we call #all
We get a list of all bookings
"""
def test_all_bookings(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    assert booking_repository.all() == [
        Booking(1 ,1, 2, 'pending'),
        Booking(2 ,1, 3, 'pending'),
        Booking(3 ,4, 2, 'confirmed'),
        Booking(4 ,4, 3, 'declined'),
        Booking(5 ,5, 1, 'confirmed'),
        Booking(6 ,6, 2, 'confirmed')
    ]

"""
When we call #find with a booking id
We get the relevant booking returned
"""
def test_find_booking(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    booking = booking_repository.find(2)
    assert booking == Booking(2 ,1, 3, 'pending')

"""
When we call #create with a booking
It gets added to the database
This is reflected when we call #all
"""
def test_create_booking(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    booking_repository.create(Booking(None, 2, 3, 'pending'))
    assert booking_repository.all() == [
        Booking(1 ,1, 2, 'pending'),
        Booking(2 ,1, 3, 'pending'),
        Booking(3 ,4, 2, 'confirmed'),
        Booking(4 ,4, 3, 'declined'),
        Booking(5 ,5, 1, 'confirmed'),
        Booking(6 ,6, 2, 'confirmed'),
        Booking(7, 2, 3, 'pending')
    ]

"""
When we call #find_all_bookings_by_user_id
We get all bookings returned by the user with the relevant id
"""
def test_find_all_bookings_and_spaces_by_user_id(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    bookings = booking_repository.find_all_bookings_and_spaces_by_user_id(2)
    assert bookings == [{'booking_id': 1, 'name': 'Beach House 1', 'space_id': 1, 'date_from': date(2025, 1, 1), 'date_to': date(2025, 1, 1), 'price_per_night': 101, 'status': 'pending'},
                        {'booking_id': 3, 'name': 'Beach House 2', 'space_id': 2, 'date_from': date(2025, 1, 2), 'date_to': date(2025, 1, 2), 'price_per_night': 102, 'status': 'confirmed'},
                        {'booking_id': 6, 'name': 'Glamping Pod 2', 'space_id': 4, 'date_from': date(2025, 1, 2), 'date_to': date(2025, 1, 2), 'price_per_night': 104, 'status': 'confirmed'}]
    
"""
When we have consecutive dates in bookings with the same space_id and user_id
When we call #find_all_bookings_by_user_id
We get all bookings returned by the user with the relevant id, with consecutive dates as part of the same request
"""
def test_find_all_bookings_and_spaces_by_user_id_with_consecutive_dates(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    booking_repository = BookingRepository(db_connection)
    spaces_repository = SpaceRepository(db_connection)
    availability_repository = AvailabilityRepository(db_connection)
    spaces_repository.create(Space(None, 1, 'Treehouse', 'A treehouse in a forrest', 200))
    availability_repository.create(Availability(None, 7, date(2023, 1, 1), True))
    availability_repository.create(Availability(None, 7, date(2023, 1, 2), True))
    availability_repository.create(Availability(None, 7, date(2023, 1, 3), True))
    booking_repository.create(Booking(None, 9, 2, 'pending'))
    booking_repository.create(Booking(None, 10, 2, 'pending'))
    booking_repository.create(Booking(None, 11, 2, 'pending'))
    bookings = booking_repository.find_all_bookings_and_spaces_by_user_id(2)
    assert bookings == [{'booking_id': 1, 'name': 'Beach House 1', 'space_id': 1, 'date_from': date(2025, 1, 1), 'date_to': date(2025, 1, 1), 'price_per_night': 101, 'status': 'pending'},
                        {'booking_id': 3, 'name': 'Beach House 2', 'space_id': 2, 'date_from': date(2025, 1, 2), 'date_to': date(2025, 1, 2), 'price_per_night': 102, 'status': 'confirmed'},
                        {'booking_id': 6, 'name': 'Glamping Pod 2', 'space_id': 4, 'date_from': date(2025, 1, 2), 'date_to': date(2025, 1, 2), 'price_per_night': 104, 'status': 'confirmed'},
                        {'booking_id': 7, 'name': 'Treehouse', 'space_id': 7, 'date_from': date(2023, 1, 1), 'date_to': date(2023, 1, 3), 'price_per_night': 200, 'status': 'pending'}]

