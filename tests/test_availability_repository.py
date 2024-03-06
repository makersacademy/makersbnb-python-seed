from lib.availability_repository import AvailabilityRepository
from lib.availability import Availability
from datetime import date

def test_all(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = AvailabilityRepository(db_connection)
    availabilities = repo.all()
    assert availabilities == [Availability(1, '2024-10-12', '2024-10-25', 1), Availability(2, '2024-05-21', '2024-06-01', 3), Availability(3, '2024-11-02', '2024-12-02', 4), Availability(4, '2024-06-10', '2024-06-28', 2)]

def test_find(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = AvailabilityRepository(db_connection)
    availability = repo.find(2)
    assert availability == Availability(2, '2024-05-21', '2024-06-01', 3)

def test_create(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = AvailabilityRepository(db_connection)
    repo.create('2024-11-27', '2024-11-30',4)
    availabilities = repo.all()
    assert availabilities == [Availability(1, '2024-10-12', '2024-10-25', 1), Availability(2, '2024-05-21', '2024-06-01', 3), Availability(3, '2024-11-02', '2024-12-02', 4), Availability(4, '2024-06-10', '2024-06-28', 2), Availability (5,'2024-11-27', '2024-11-30',4)]
  
def test_update(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = AvailabilityRepository(db_connection)
    availability = repo.find(1)
    availability.availability_from = '2024-10-17'
    availability.availability_to = '2024-10-27'
    repo.update(availability)
    result = repo.find(1)
    assert result == Availability(1, '2024-10-17', '2024-10-27', 1)

def test_delete(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = AvailabilityRepository(db_connection)
    repo.delete(4)
    assert repo.all() == [Availability(1, '2024-10-12', '2024-10-25', 1), Availability(2, '2024-05-21', '2024-06-01', 3), Availability(3, '2024-11-02', '2024-12-02', 4)]