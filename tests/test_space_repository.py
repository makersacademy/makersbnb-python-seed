from lib.space_repository import *
from lib.space import *
from datetime import date

def test_add_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    space = Space(None, 'test description', 99.99, 1, 'test name', date(2024, 1, 1), date(2024, 1, 31))
    repository.add(space)
    result = repository.all()
    assert space.id == 3
    assert result == [Space(1, 'house with a pool', 99.99, 1, 'pool house', date(2024, 3, 4), date(2024, 3, 31)), Space(2, 'house with a garden', 199.99, 2, 'garden house', date(2024, 4, 1), date(2024, 4, 30)), Space(3, 'test description', 99.99, 1, 'test name', date(2024, 1, 1), date(2024, 1, 31))]

def test_all(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Space(1, 'house with a pool', 99.99, 1, 'pool house', date(2024, 3, 4), date(2024, 3, 31)), Space(2, 'house with a garden', 199.99, 2, 'garden house', date(2024, 4, 1), date(2024, 4, 30))]

# def test_find():
#     db_connection.seed('seeds/makersbnb.sql')
#     repository = SpaceReposiotiry(db_connection)
#     filtered_spaces = repository.filter()
#     assert filtered_spaces ==