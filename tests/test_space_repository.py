from lib.space import Space
from lib.space_repository import SpaceRepository

"""When I call #all in the SpaceRepository 
I get all the Spaces back in the list"""

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.all()
    assert result == [
        Space(1, "space_1", "description_1", 45.50, 1),
        Space(2, "space_2", "description_2", 14000.99, 2)
    ]


"""When we call #find in SpaceRepository with a 
specific id we are presented with the Space attached to 
this id"""

def test_find_space_with_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    result = repository.find(1)
    assert result == Space(1, 'space_1', 'description_1', 45.50, 1)

def test_create(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    space = Space(None, "mybnb", "in beverley hills", 9000, 2)
    repository.create(space)
    assert space.id == 3
    assert repository.all() == [
        Space(1, "space_1", "description_1", 45.50, 1),
        Space(2, "space_2", "description_2", 14000.99, 2),
        Space(3, "mybnb", "in beverley hills", 9000.0, 2)
    ]
