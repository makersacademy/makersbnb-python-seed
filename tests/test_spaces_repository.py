from lib.spaces_repository import SpacesRepository
from lib.space import Space
import datetime


"""
list all spaces
"""

def test_list_all_space(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpacesRepository(db_connection)
    all_listings = repository.all_listings()
    space1 = Space(1, 'Apartment 1', 'Description 1', 100, datetime.date(2024, 1, 1), datetime.date(2024, 1, 1), 1)
    assert space1.price == all_listings[0].price
    assert space1.date_from == all_listings[0].date_from
    
    
    assert repository.all_listings() == [Space(1, 'Apartment 1', 'Description 1', 100, datetime.date(2024, 1, 1), datetime.date(2024, 4, 1), 1),
                                Space(2, 'Apartment 2', 'Description 2', 200, datetime.date(2024, 1, 1), datetime.date(2024, 4, 1), 2) 
                            ]



"""
add new spaces

"""

def test_add_new_space_listing(db_connection):
    db_connection.seed("seeds/spaces.sql")
    new_listing = Space(3, 'Apartment 3', 'Description 3', 100, datetime.date(2024, 1, 1), datetime.date(2024, 2, 3),3)
    repository =  SpacesRepository(db_connection)
    repository.create_listing(new_listing)
    assert new_listing.price == repository.all_listings()[2].price
    # assert new_listing.date_from == repository.all_listings()[2].date_from
    # assert new_listing.date_to == repository.all_listings()[2].date_to
    # assert repository.all_listings() == [
    #     Space(1, 'Apartment 1', 'Description 1', 100, datetime.date(2024, 1, 1), datetime.date(2024, 4, 1),1),
    #     Space(2, 'Apartment 2', 'Description 2', 200, datetime.date(2024, 1, 1), datetime.date(2024, 4, 1),2),
    #     Space(3, 'Apartment 3', 'Description 3', 100, datetime.date(2024, 1, 1), datetime.date(2024, 2, 3),3)
    #                         ]

    