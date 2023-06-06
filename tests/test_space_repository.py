from lib.space import Space
from lib.space_repository import SpaceRepository

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/users_spaces.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()
    assert spaces == [
        Space(1, "test_title", "test_description", "$50.00", "2023-01-08", 1),
        Space(2, "test_title2", "test_description2", "$60.00", "2023-05-10", 1)
    ]