from lib.spaces_repository import *
from lib.spaces import *

"""
When we call the space repo,
we should be able to connect successfully,
so that we should be able to access a list of spaces.
"""
def test_database_connects_successfully(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = SpaceRepository(db_connection)
    assert (type(repo.list_all_spaces()) == list)
    assert (len(repo.list_all_spaces()) is not 0)

"""""
When we add a space to the repo,
it should successfully be stored in the repo,
so that we can access the space.
"""
def test_add_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = SpaceRepository(db_connection)

    test_space = Space(9, "testspace1", "test", 1.5, 1)
    repo.add_space(test_space)
    assert len(repo.list_all_spaces()) == 6

"""
When we call Space_Repository#get_space_by_id
we get a single space object
"""
def test_get_space_by_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = SpaceRepository(db_connection)
    # test_space = Space(1, "testspace1", "test", 1.5, 1)
    # repo.add_space(test_space)
    space = repo.get_space_by_id(1)
    assert space == Space(1, '1 Test Drive', 'A small one bedroom flat with wet room and kitchenette.', 50.00, 1)

"""
When we call Space_Repository#get_space_by_host_id
we get a list of space objects with the same host_id
"""
def test_get_spaces_by_host_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = SpaceRepository(db_connection)
    spaces = repo.get_spaces_by_host_id(1)
    # 50.00 does not carry significant information in 2nd decimal place 
    # and is getting truncated. Format forces this to be a string.
    # Therefore, must compare strings in assertion.
    assert [str(space) for space in spaces] == [
        str(Space(1, '1 Test Drive', 'A small one bedroom flat with wet room and kitchenette.', "{:.2f}".format(50.00), 1)),
        str(Space(2, '2 Notteven Close', '3 bed, 3 bath, 3 beyond?', 115.99, 1))
    ]
"""
When we call SpaceRepository#all
We get a list of objects back reflecting the seed
"""
def test_list_all_spaces_returns_a_list(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = SpaceRepository(db_connection)
    spaced = repo.list_all_spaces()
    assert (len(spaced) is not 0)

"""
When we call SpaceRepository#get_available_dates
We get a list of dates back that the space is available to book
"""
def test_get_available_dates(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repo = SpaceRepository(db_connection)
    dates = repo.get_available_dates(3)
    assert len(dates) == 5