from lib.date_repositoty import DateRepository

"""
When I call date repo #alldates 
I get a list of all dates from date tabla
"""

def test_all(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repo = DateRepository(db_connection)

    assert repo.all() == [
        Date('2023-10-24', True, 3),
        Date('2023-10-25', True, 5),
        Date('2023-10-26', True, 2),
        Date('2023-10-27', True, 3),
        Date('2023-10-28', False, 5),
        Date('2023-10-29', False, 1),
        Date('2023-10-30', False, 1),
        Date('2023-10-01', False, 3),
        Date('2023-10-02', False, 4),
        Date('2023-10-03', False, 2)
    ]