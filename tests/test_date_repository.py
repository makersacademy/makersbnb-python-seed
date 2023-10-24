from lib.date_repositoty import DateRepository
from lib.date import Date


"""
When I call date repo #alldates 
I get a list of all dates from date tabla
"""

def test_all(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.all() == [
        Date(1, '2023-10-24', True, 3),
        Date(2, '2023-10-25', True, 5),
        Date(3, '2023-10-26', True, 2),
        Date(4, '2023-10-27', True, 3),
        Date(5, '2023-10-28', False, 5),
        Date(6, '2023-10-29', False, 1),
        Date(7, '2023-10-30', False, 1),
        Date(8, '2023-10-01', False, 3),
        Date(9, '2023-10-02', False, 4),
        Date(10, '2023-10-03', False, 2)
    ]

"""
When calling #find with id
I get a specific date back
"""

def test_find_with_id(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.find_with_id(1) ==  Date(1, '2023-10-24', True, 3)

def test_find_with_date(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.find_with_date('2023-10-24', True) == [
        Date(1, '2023-10-24', True, 3)
    ]

# Wheb find with date is called and there is no availability nothing is returned
def test_find_with_unavailable_date(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.find_with_date('2023-10-28', True) == []

def test_find_if_available(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.find_by_available(True) == [
        Date(1, '2023-10-24', True, 3),
        Date(2, '2023-10-25', True, 5),
        Date(3, '2023-10-26', True, 2),
        Date(4, '2023-10-27', True, 3)
    ]

def test_create(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    date = Date(None, '2023-10-07', True, 4)

    repo.create(date)

    assert date.id == 11
    assert repo.all() == [
        Date(1, '2023-10-24', True, 3),
        Date(2, '2023-10-25', True, 5),
        Date(3, '2023-10-26', True, 2),
        Date(4, '2023-10-27', True, 3),
        Date(5, '2023-10-28', False, 5),
        Date(6, '2023-10-29', False, 1),
        Date(7, '2023-10-30', False, 1),
        Date(8, '2023-10-01', False, 3),
        Date(9, '2023-10-02', False, 4),
        Date(10, '2023-10-03', False, 2),
        Date(11, '2023-10-07', True, 4)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    repo.delete_individual(10)

    assert repo.all() == [
        Date(1, '2023-10-24', True, 3),
        Date(2, '2023-10-25', True, 5),
        Date(3, '2023-10-26', True, 2),
        Date(4, '2023-10-27', True, 3),
        Date(5, '2023-10-28', False, 5),
        Date(6, '2023-10-29', False, 1),
        Date(7, '2023-10-30', False, 1),
        Date(8, '2023-10-01', False, 3),
        Date(9, '2023-10-02', False, 4)
    ]

def test_delete_all_dates_for_space(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    repo.delete_by_space(3)

    assert repo.all() == [
        Date(2, '2023-10-25', True, 5),
        Date(3, '2023-10-26', True, 2),
        Date(5, '2023-10-28', False, 5),
        Date(6, '2023-10-29', False, 1),
        Date(7, '2023-10-30', False, 1),
        Date(9, '2023-10-02', False, 4),
        Date(10, '2023-10-03', False, 2)
    ]