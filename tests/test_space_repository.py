from lib.space_repository import SpaceRepository
from lib.space import Space

def test_all(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)
    spaces = repo.all()
    assert spaces == [Space(1, 'London Bridge', 15.99, 'It isnt the one you think it is', 1), Space(2, 'Big Ben', 97.43, 'Tall clock, its loud', 3), Space(3, 'Gherkin', 46.90, 'Americans call it the pickle', 2), Space(4, 'The Shard', 546.00, 'The sky garden is free', 2)]

def test_find(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)
    space = repo.find(3)
    assert space == Space(3, 'Gherkin', 46.90, 'Americans call it the pickle', 2)

def test_create(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)
    repo.create('my house', 13.21,'its my house', 3)
    spaces = repo.all()
    assert spaces == [Space(1, 'London Bridge', 15.99, 'It isnt the one you think it is', 1), Space(2, 'Big Ben', 97.43, 'Tall clock, its loud', 3), Space(3, 'Gherkin', 46.90, 'Americans call it the pickle', 2), Space(4, 'The Shard', 546.00, 'The sky garden is free', 2), Space(5, "my house", 13.21, 'its my house', 3)]
  
def test_update(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)
    space = repo.find(1)
    space.price = 22.22
    repo.update(space)
    result = repo.find(1)
    assert result == Space(1, 'London Bridge', 22.22, 'It isnt the one you think it is', 1)

def test_delete(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repo = SpaceRepository(db_connection)
    repo.delete(1)
    assert repo.all() == [Space(2, 'Big Ben', 97.43, 'Tall clock, its loud', 3), Space(3, 'Gherkin', 46.90, 'Americans call it the pickle', 2), Space(4, 'The Shard', 546.00, 'The sky garden is free', 2)]