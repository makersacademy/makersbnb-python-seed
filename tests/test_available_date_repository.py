from lib.available_date_repository import AvailableDateRepository
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