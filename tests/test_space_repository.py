from lib.space import Space
from lib.space_repository import SpaceRepository

"""
When we add a Space object, we are able to view all the objects
"""

def test_all_spaces(db_connection):
    db_connection.seed('seeds/spaces_table.sql')
    repo = SpaceRepository(db_connection)
    assert repo.all() == [
        Space(1, 'Name1', 'Description of space', 20),
        Space(2, 'Name2', 'Another description of space', 30),
    ]