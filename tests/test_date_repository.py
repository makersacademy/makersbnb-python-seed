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