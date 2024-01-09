from lib.spaces_repository import *
from lib.spaces import *

"""
When we call the space repo,
we should be able to connect successfully,
so that we should be able to access a list of spaces.
"""
def test_database_connects_successfully(db_connection):
    db_connection.seed("")
    repo = SpaceRepository(db_connection)
    assert (type(repo.all()) == "list")
    assert (len(repo.all()) is not 0)

"""""
When we add a space to the repo,
it should successfully be stored in the repo,
so that we can access the space.
"""
def test_add_space(db_connection):
    db_connection.seed("")
    repo = SpaceRepository(db_connection)

    test_space = Space(1, "TestSpace1", "test", 1.5, 1)
    repo.add_space(test_space)
    assert len(repo.list_all_spaces()) == 1

"""
When we call Space_Repository#get_space_by_id
we get a single space object
"""
def test_get_space_by_id(db_connection):
    db_connection.seed('')
    repo = SpaceRepository(db_connection)
    test_space = Space(1, "TestSpace1", "test", 1.5, 1)
    repo.add_space(test_space)
    space = repo.get_space_by_id(1)
    assert space == test_space

"""
When we call SpaceRepository#all
We get a list of objects back reflecting the seed
"""
def test_list_all_spaces_returns_a_list(db_connection):
    db_connection.seed('')
    repo = SpaceRepository(db_connection)
    spaced = repo.list_all_spaces()
    assert (len(repo.all()) is not 0)