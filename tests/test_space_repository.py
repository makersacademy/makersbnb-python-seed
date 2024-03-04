from lib.space_repository import *
from lib.space import *

def test_add_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    space = Space(None, 'test description', 99.99, 1, 'test name')
    repository.add(space)
    result = repository.all()
    assert space.id == 3
    assert result == [Space(1, 'house with a pool', 99.99, 1, 'pool house'), Space(2, 'house with a garden', 199.99, 2, 'garden house'), Space(3, 'test description', 99.99, 1, 'test name')]

def test_all(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Space(1, 'house with a pool', 99.99, 1, 'pool house'), Space(2, 'house with a garden', 199.99, 2, 'garden house')]

# def test_filter():
#     db_connection.seed('seeds/makersbnb.sql')
#     repository = SpaceReposiotiry(db_connection)
#     filtered_spaces = repository.filter()
#     assert filtered_spaces ==