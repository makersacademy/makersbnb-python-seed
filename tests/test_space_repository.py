from lib.space_repository import SpaceRepository
from lib.space import Space
"""
all()
"""

def test_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    rows = repo.all() # a list of space objects
    assert rows == [
        Space(1, 'space_1',	'A nice space',	10,	1),
        Space(2, 'space_2', 'Another nice space', 20, 2),
    ]


"""
find(id) => finds a Space object given their id
"""

def test_find_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    row = repo.find(2)
    assert row == Space(2, 'space_2', 'Another nice space', 20, 2)


"""
create(space_name, description, price_per_night, user_id)
"""

def test_create_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    space3 = Space(None, 'test name5', 'test description5', 30 , 2)
    repo.create(space3)
    rows = repo.all()
    assert rows[2] == Space(3, 'test name5', 'test description5', 30 , 2)

"""
delete(id)
"""

def test_delete_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    repo.delete(1)
    rows = repo.all()
    assert rows == [
        Space(2, 'space_2', 'Another nice space', 20, 2),
    ]
