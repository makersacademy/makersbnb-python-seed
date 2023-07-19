from lib.space_repository import *

def test_all_method(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Space(1, 'Example bnb', 'Examply cosy bnb', 100, '18/07/23, 19/07/23, 20/07/23', 2)]

def test_create_method(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(2, 'Example bnb 2', 'Examply very cosy bnb', 100, '19/07/23', 3))
    spaces = repository.all()
    assert spaces == [Space(1, 'Example bnb', 'Examply cosy bnb', 100, '18/07/23, 19/07/23, 20/07/23', 2),
                    Space(2, 'Example bnb 2', 'Examply very cosy bnb', 100, '19/07/23', 3)]

def test_find_method_works(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(2, 'Example bnb 2', 'Examply very cosy bnb', 100, '19/07/23', 3))
    space_found = repository.find(1)
    assert space_found == [Space(1, 'Example bnb', 'Examply cosy bnb', 100, '18/07/23, 19/07/23, 20/07/23', 2)]