from lib.date import *
from lib.date_repository import *

"""
When i call #all on the date repository
I get all of the dates
"""
def test_list_all_dates(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = DateRepository(db_connection)
    result = repository.all()
    assert result == [
        Date(1, '2024-01-20', True, 1),
        Date(2, '2024-01-21', False, 2),
        Date(3, '2024-01-22', False, 2),
        Date(4, '2024-01-23', True, 3),
        Date(5, '2024-01-24', False, 1),
        Date(6, '2025-01-25', False, 4)
    ]

"""
When i call #find on the date repository
I get the date with the matching id
"""

def test_find_date(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = DateRepository(db_connection)
    result = repository.find(1)
    assert result == Date(1, '2024-01-20', True, 1)

"""
When i call #create on the date repository
I create a new date
"""

def test_create_date(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = DateRepository(db_connection)
    repository.create(Date(None, '2024-01-26', False, 1))
    result = repository.all()
    assert result == [
        Date(1, '2024-01-20', True, 1),
        Date(2, '2024-01-21', False, 2),
        Date(3, '2024-01-22', False, 2),
        Date(4, '2024-01-23', True, 3),
        Date(5, '2024-01-24', False, 1),
        Date(6, '2025-01-25', False, 4),
        Date(7, '2024-01-26', False, 1)
    ]

"""
When i call #delete on the date repository
I delete the date with the matching id
"""  

def test_delete_date(db_connection):
    db_connection.seed("seeds/makersbnb_seeds.sql")
    repository = DateRepository(db_connection)
    repository.delete(1)
    result = repository.all()
    assert result == [
        Date(2, '2024-01-21', False, 2),
        Date(3, '2024-01-22', False, 2),
        Date(4, '2024-01-23', True, 3),
        Date(5, '2024-01-24', False, 1),
        Date(6, '2025-01-25', False, 4)
    ]