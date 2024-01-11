from lib.availability import Availability
from lib.availability_repository import AvailabilityRepository
from datetime import date

# CREATE TABLE availability (
#     id SERIAL NOT NULL UNIQUE,
#     space_id int,
#     date date,
#     status boolean,
#     primary key (space_id, date),
#     constraint fk_space foreign key(space_id) references spaces(id) on delete cascade
# );

"""
When we call AvailabilityRepository#all
We get a list of Available list of spaces reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/makers_bnb.sql") # Seed our database with some test data
    repository = AvailabilityRepository(db_connection) # Create a new AvailabilityRepository

    availablespaces = repository.all() # Get all spaces

    # Assert on the results
    assert availablespaces == [
        Availability(1, 1, date(2025,1,1), True),
        Availability(2, 1, date(2025,1,2), True),
        Availability(3, 1, date(2025,2,3), True),
        Availability(4, 2, date(2025,1,2), True),
        Availability(5, 3, date(2025,1,2), True),
        Availability(6, 4, date(2025,1,2), True),
        Availability(7, 5, date(2025,1,2), True),
        Availability(8, 6, date(2025,1,2), True)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") # Seed our database with some test data
    repository = AvailabilityRepository(db_connection) # Create a new AvailabilityRepository

    space = Availability(None, 5, date(2025,2,2))
    repository.create(space)

    availablespaces = repository.all() # Get all spaces

    # Assert on the results
    assert availablespaces == [
        Availability(1, 1, date(2025,1,1), True),
        Availability(2, 1, date(2025,1,2), True),
        Availability(3, 1, date(2025,2,3), True),
        Availability(4, 2, date(2025,1,2), True),
        Availability(5, 3, date(2025,1,2), True),
        Availability(6, 4, date(2025,1,2), True),
        Availability(7, 5, date(2025,1,2), True),
        Availability(8, 6, date(2025,1,2), True),
        Availability(9, 5, date(2025,2,2), True)
    ]