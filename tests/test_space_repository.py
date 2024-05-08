from lib.spaces import *
from lib.space_repository import *

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
            Space(1, 1, 'venue #1', 'desc #1', 50, True),
            Space(2, 1, 'venue #2', 'desc #2', 60, True),
            Space(3, 1, 'venue #3', 'desc #3', 70, True),
            Space(4, 2, 'venue #4', 'desc #4', 80, True),
            Space(5, 2, 'venue #5', 'desc #5', 90, True)
        ]

def test_create_spaces(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 2, 'venue #6', 'desc #6', 50, True))
    result = repository.all()
    assert repository.all() == [
            Space(1, 1, 'venue #1', 'desc #1', 50, True),
            Space(2, 1, 'venue #2', 'desc #2', 60, True),
            Space(3, 1, 'venue #3', 'desc #3', 70, True),
            Space(4, 2, 'venue #4', 'desc #4', 80, True),
            Space(5, 2, 'venue #5', 'desc #5', 90, True),
            Space(6, 2, 'venue #6', 'desc #6', 50, True)
        ]

def test_find(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = SpaceRepository(db_connection)
    result = repository.find(3)
    assert result == Space(3, 1, 'venue #3', 'desc #3', 70, True)

def test_delete(db_connection):
    db_connection.seed("seeds/seed.sql")
    repository = SpaceRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
            Space(1, 1, 'venue #1', 'desc #1', 50, True),
            Space(2, 1, 'venue #2', 'desc #2', 60, True),
            Space(4, 2, 'venue #4', 'desc #4', 80, True),
            Space(5, 2, 'venue #5', 'desc #5', 90, True)
        ]

