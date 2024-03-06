from lib.space import Space
from lib.space_repository import SpaceRepository

"""
When we call SpaceRepository#all
We get a list of Space objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [
        Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1),
        Space(2, 'Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00, 2)
    ]

"""
When we call SpaceRepository#find
We get a single Space object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find(2)
    assert space == Space(2, 'Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00, 2)

"""
When we call SpaceRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = SpaceRepository(db_connection)

    repository.create(Space(None, 'test apartment', 'test description', 200.00, 2))

    result = repository.all()
    assert result == [
        Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', 120.00, 1),
        Space(2, 'Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00, 2),
        Space(3, 'test apartment', 'test description', 200.00, 2)
    ]

# """
# When we call SpaceRepository#delete
# We remove a record from the database.
# """
def test_delete_record(db_connection):
    db_connection.seed("seeds/bnb_table.sql")
    repository = SpaceRepository(db_connection)
    repository.delete(1)

    result = repository.all()
    assert result == [
        Space(2, 'Luxurious apartment', 'Stunning luxurious apartment in the city center.', 250.00, 2)
    ]