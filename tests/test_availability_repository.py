from lib.availability import Availability
from lib.availability_repository import AvailabilityRepository


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
        Availability(1,"2025-01-01",True),
        Availability(1,"2025-01-02",True),
        Availability(1,"2025-01-03",True),
        Availability(2,"2025-01-02",True),
        Availability(3,"2025-01-02",True),
        Availability(4,"2025-01-02",True),
        Availability(5,"2025-01-02",True),
        Availability(6,"2025-01-02",True)
    ]