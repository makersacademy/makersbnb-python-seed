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
        Space(1, 'test name1', 'test description1', 30 , 1),
        Space(2, 'test name2', 'test description2', 30 , 1),
        Space(3, 'test name3', 'test description3', 30 , 2),
        Space(4, 'test name4', 'test description4', 30 , 3)
    ]


"""
find(id) => finds a Space object given their id
"""

def test_find_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    row = repo.find(2)
    assert row == Space(2, 'test name2', 'test description2', 30 , 1)


"""
create(space_name, description, price_per_night, user_id)
"""

def test_create_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    space5 = Space(None, 'test name5', 'test description5', 30 , 4)
    repo.create(space5)
    rows = repo.all()
    assert rows[4] == Space(5, 'test name5', 'test description5', 30 , 4)

"""
delete(id)
"""

def test_delete_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repo = SpaceRepository(db_connection)
    repo.delete(1)
    rows = repo.all()
    assert rows == [
        Space(2, 'test name2', 'test description2', 30 , 1),
        Space(3, 'test name3', 'test description3', 30 , 2),
        Space(4, 'test name4', 'test description4', 30 , 3)
    ]
