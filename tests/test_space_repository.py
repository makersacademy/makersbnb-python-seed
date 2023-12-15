from lib.space_repository import *
from lib.space import *
from datetime import datetime
"""
We can call #SpaceRepository and
We get all the seed data back
"""

def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = SpaceRepository(db_connection)

    space = repository.all()

    assert space == [
        Space(1, 'Bagend', 'Hobbit Hole', 50, '25-12-23', '30-12-23'),
        Space(2, 'Isengard', 'Wizards Tower', 150, '25-12-23', '30-12-23'),
        Space(3, 'Minas Tirith', 'Big White City', 200, '25-12-23', '30-12-23')
    ]

"""
When we call #find function
we get single space returned 
"""
def test_find_since_space(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repository = SpaceRepository(db_connection)
    space = repository.find(2)
    assert space == Space(2, 'Isengard', 'Wizards Tower', 150, '25-12-23', '30-12-23')
    


"""
When we call SpaceRepository
#create
We get a new spcae added in the database
"""
def test_create_space(db_connection):
    db_connection.seed("seeds/bnb.sql")
    repository = SpaceRepository(db_connection)

    repository.create(Space(None, "Rivendale", "Wood Elves", 300, '25-12-23', '30-12-23'))

    result = repository.all()
    assert result == [
        Space(1, 'Bagend', 'Hobbit Hole', 50, '25-12-23', '30-12-23'),
        Space(2, 'Isengard', 'Wizards Tower', 150, '25-12-23', '30-12-23'),
        Space(3, 'Minas Tirith', 'Big White City', 200, '25-12-23', '30-12-23'),
        Space(4, "Rivendale", "Wood Elves", 300, '25-12-23', '30-12-23')]