from lib.request_repository import RequestRepository
from lib.request import Request
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = RequestRepository(db_connection)
    assert repository.all() == [Request(1, 1, 1, "01/01/2023", "TBC")]

"""
When we choose avaliable date,
we create a request to book a space
"""
def test_create_request(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = RequestRepository(db_connection)
    repository.create(Request(None, 2, 1, "01/01/2023", "TBC"))
    result = repository.all()
    assert result == [Request(1, 1, 1, "01/01/2023", "TBC"), Request(2, 2, 1, "01/01/2023", "TBC")]

def test_find_request(db_connection):
    repository = RequestRepository(db_connection)
    repository.create(Request(None, 1, 1, "01/01/2023", "TBC"))
    assert repository.find(1) == Request(1, 1, 1, "01/01/2023", "TBC")

def test_confirm_a_request(db_connection):
    repository = RequestRepository(db_connection)
    request = Request(None, 1, 1, "01/01/2023", "TBC")
    repository.create(request)
    request_1 = repository.find(1)
    repository.confirm_booking(request_1)
    assert request_1.request_status == "True"

    
def test_decline_a_request(db_connection):
    repository = RequestRepository(db_connection)
    request = Request(None, 1, 1, "01/01/2023", "TBC")
    repository.create(request)
    request_1 = repository.find(1)
    repository.decline_a_request(request_1)
    assert request_1.request_status == "False"
    
def test_find_spaces_by_user_id(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = RequestRepository(db_connection)
    space_repository = SpaceRepository(db_connection)
    user_repository = UserRepository(db_connection)

    space_2 = Space(None,"Example Name","Example description",200,"02-03-2023",1)
    space_repository.create(space_2)

    user_3 = User(None, "Example user3", "examplepassword3", "exampleemail3@email.com")
    user_4 = User(None, "Example user4", "examplepassword4", "exampleemail4@email.com")
    user_repository.create(user_3)
    user_repository.create(user_4)

    repository.create(Request(None, 3, 1, "01/01/2023", "TBC"))
    repository.create(Request(None, 3, 2, "01/01/2023", "TBC"))
    repository.create(Request(None, 4, 1, "01/01/2023", "TBC"))
    repository.create(Request(None, 4, 2, "01/01/2023", "TBC"))
    print(repository.find_spaces_by_user_id(2))
    assert repository.find_spaces_by_user_id(2) == [Request(2, 1, 1, '01/01/2023', 'TBC'),
            Request(3, 1, 1, '01/01/2023', 'TBC'),
            Request(4, 3, 1, '01/01/2023', 'TBC'),
            Request(6, 4, 1, '01/01/2023', 'TBC'),
            Request(8, 3, 1, '01/01/2023', 'TBC'),
            Request(10, 4, 1, '01/01/2023', 'TBC')]

