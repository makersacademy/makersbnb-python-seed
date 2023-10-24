from lib.available_date_repository import AvailableDateRepository
from lib.available_date import AvailableDate
"""
test construction
"""
def test_init_method_connection_params(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    example_date_repo = AvailableDateRepository(db_connection)
    assert example_date_repo._connection == db_connection

"""
test #all method
"""
def test_all_method_return(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    example_date_repo = AvailableDateRepository(db_connection)
    assert example_date_repo.all() == [AvailableDate(1, '12/11/03', 1), AvailableDate(2, '11/11/00', 2)]
