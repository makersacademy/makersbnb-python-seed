from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.user_repository import UserRepository
from playwright.sync_api import Page, expect

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/users_spaces.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()
    assert spaces == [
        Space(1, "test_title", "test_description", "$50.00", "2023-01-08", 1),
        Space(2, "test_title2", "test_description2", "$60.00", "2023-05-10", 1)
    ]

def test_create_a_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_spaces.sql")
    space_repo = SpaceRepository(db_connection)
    user_repo = UserRepository(db_connection)

    user_repo.create_user(User(None, 'firstname', 'lastname', 'test@test.com', 'password'))
    space_repo.create(Space(None, 'london', 'a nice hotel', '$65.00', '2023-06-10', 1))

    spaces = space_repo.all()
    assert spaces == [
        Space(1, "test_title", "test_description", "$50.00", "2023-01-08", 1),
        Space(2, "test_title2", "test_description2", "$60.00", "2023-05-10", 1),
        Space(3, "london", "a nice hotel", "$65.00", "2023-06-10", 1)
    ]

