from lib.space_repository import SpaceRepository
from lib.space import Space


def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [Space(1, "3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01"),
                      Space(2, "Penthouse", "Manchester", "city", 150, 1, "2024-03-01", "2025-01-01"),
                      Space(3, "BnB villa", "Rome", "city", 300, 1, "2024-02-01", "2024-09-01"),
                      Space(4, "Town cottage", "Newastle", "city", 125, 1, "2024-03-01", "2024-11-01")]



def test_create_space(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    new_space = Space(5, "mountain view", "Ben Nevis", "mountain", 150, 1, "2024-03-01", "2025-03-01")

    repository.create(new_space)

    result = repository.all()

    assert result == [
        Space(1, "3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01"),
                      Space(2, "Penthouse", "Manchester", "city", 150, 1, "2024-03-01", "2025-01-01"),
                      Space(3, "BnB villa", "Rome", "city", 300, 1, "2024-02-01", "2024-09-01"),
                      Space(4, "Town cottage", "Newastle", "city", 125, 1, "2024-03-01", "2024-11-01"),
                      Space(5, "mountain view", "Ben Nevis", "mountain", 150, 1, "2024-03-01", "2025-03-01")
    ]


def test_find_by_id(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find_by_id(1)

    assert space[0] == Space(1,"3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01")


def test_find_by_price(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find_by_price(200)

    assert space[0] == Space(1,"3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01")


def test_delete_space(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    repository.delete(2)

    result = repository.all()

    assert result == [Space(1,"3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01"),
                      Space(3, "BnB villa", "Rome", "city", 300, 1, "2024-02-01", "2024-09-01"),
                      Space(4, "Town cottage", "Newastle", "city", 125, 1, "2024-03-01", "2024-11-01")]

def test_find_by_date(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    result = repository.find_by_date("2024-02-07")

    assert result == [Space(1,"3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01"),
                      Space(3, "BnB villa", "Rome", "city", 300, 1, "2024-02-01", "2024-09-01")
                      ]


def test_find_by_space_name(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    space = repository.find_by_space_name("3 bedroom apartment")

    assert space[0] == Space(1,"3 bedroom apartment", "London", "city", 200, 1, "2024-02-01", "2025-02-01")


def test_empty_all_function(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    repository.delete(1)
    repository.delete(2)
    repository.delete(3)
    repository.delete(4)

    spaces = repository.all()

    assert spaces == "No results found"

    spaces = repository.find_by_date("2013-02-19")

    assert spaces == "No results found"

    spaces = repository.find_by_id(28)

    assert spaces == "No results found"

    spaces = repository.find_by_price(1)

    assert spaces == "No results found"

    spaces = repository.find_by_space_name("koala")

    assert spaces == "No results found"