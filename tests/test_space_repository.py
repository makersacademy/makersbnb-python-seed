from lib.space_repository import SpaceRepository
from lib.space import Space


def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [Space(1, "London", "city", 200, 1, "2024-02-01", "2025-02-01")]


def test_create_space(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    new_space = Space(2, "Ben Nevis", "mountain", 150, 1, "2024-03-01", "2025-03-01")

    repository.create(new_space)

    result = repository.all()

    assert result == [
        Space(1, "London", "city", 200, 1, "2024-02-01", "2025-02-01"),
        Space(2, "Ben Nevis", "mountain", 150, 1, "2024-03-01", "2025-03-01"),
    ]


def test_find_by_id(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find_by_id(1)

    assert space[0] == Space(1, "London", "city", 200, 1, "2024-02-01", "2025-02-01")


def test_find_by_price(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find_by_price(200)

    assert space[0] == Space(1, "London", "city", 200, 1, "2024-02-01", "2025-02-01")


def test_delete_space(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    repository.delete(2)

    result = repository.all()

    assert result == [Space(1, "London", "city", 200, 1, "2024-02-01", "2025-02-01")]
