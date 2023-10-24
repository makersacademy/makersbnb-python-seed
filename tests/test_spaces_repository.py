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
    space1 = Space(1, 'Apartment 1', 'Description 1', 100, datetime.date(2024, 1, 1), datetime.date(2024, 1, 1))
    assert space1.price == all_listings[0].price
    assert space1.date_from == all_listings[0].date_from
    
    
    repository.all_listings() == [Space(1, 'Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01'),
                                Space(2, 'Apartment 2', 'Description 2', 200, '2024-01-01', '2024-04-01') 
                                
                                ]



"""
add new spaces

"""


