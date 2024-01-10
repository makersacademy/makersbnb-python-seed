from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.availability import Availability
from datetime import date

"""
When we call #all
We get a list of all spaces
"""
def test_all_spaces(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    space_repository = SpaceRepository(db_connection)
    assert space_repository.all() == [
        Space(1, 1, 'Beach House 1', 'A beautiful beach side property with a pool', 101),
        Space(2, 1, 'Beach House 2', 'A beautiful beach side property with a pool', 102),
        Space(3, 2, 'Glamping Pod 1', 'A glamping pod with all cooking facilities', 103),
        Space(4, 2, 'Glamping Pod 2', 'A glamping pod with all cooking facilities', 104),
        Space(5, 3, 'Country escape 1', 'A luxury cottage in the middle of the countryside', 105),
        Space(6, 3, 'Country escape 2', 'A luxury cottage in the middle of the countryside', 106),
    ]

"""
When we call #find with a space id
We get a single space with the relevant id
"""
def test_find_space(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    space_repository = SpaceRepository(db_connection)
    space = space_repository.find(3)
    assert space == Space(3, 2, 'Glamping Pod 1', 'A glamping pod with all cooking facilities', 103)

"""
when we call #create with a space
The space is added to the spaces database
This is reflected when we call #all
"""
def test_create_space(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    space_repository = SpaceRepository(db_connection)
    space_repository.create(Space(None, 2, 'Treehouse', 'A small treehouse in a local forrest.', 150))
    assert space_repository.all() == [
        Space(1, 1, 'Beach House 1', 'A beautiful beach side property with a pool', 101),
        Space(2, 1, 'Beach House 2', 'A beautiful beach side property with a pool', 102),
        Space(3, 2, 'Glamping Pod 1', 'A glamping pod with all cooking facilities', 103),
        Space(4, 2, 'Glamping Pod 2', 'A glamping pod with all cooking facilities', 104),
        Space(5, 3, 'Country escape 1', 'A luxury cottage in the middle of the countryside', 105),
        Space(6, 3, 'Country escape 2', 'A luxury cottage in the middle of the countryside', 106),
        Space(7, 2, 'Treehouse', 'A small treehouse in a local forrest.', 150)
    ]

"""
When we call #find_space_with_availabilities
We get a single space with all the availabilities where status = True
"""
def test_find_space_with_availabilities(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    space_repository = SpaceRepository(db_connection)
    space, availability = space_repository.find_space_with_availabilities(1)
    assert space == Space(1, 1, 'Beach House 1', 'A beautiful beach side property with a pool', 101) 
    assert availability == [
        Availability(1, date(2025,1,1), True),
        Availability(2, date(2025,1,2), True),
        Availability(3, date(2025,1,3), True)
        ]
    