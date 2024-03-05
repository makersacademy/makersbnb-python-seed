from lib.space_repository import *
from lib.space import *

def test_add_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)

    space = Space(None, 'test description', 99.99, 1, 'test name', '01-01-2024', '31-01-2024')
    print("HERE!!!!!")
    print(space.free_dates)
    repository.add(space)
    result = repository.all()
    assert space.id == 3
    assert result == [Space(1, 'house with a pool', 99.99, 1, 'pool house', '04-03-2024', '31-03-2024'), Space(2, 'house with a garden', 199.99, 2, 'garden house', '01-04-2024', '30-04-2024'), Space(3, 'test description', 99.99, 1, 'test name', '01-01-2024', '31-01-2024')]

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