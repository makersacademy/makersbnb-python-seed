import os
from lib.properties_repository import *
from lib.properties import *


"""
Given 5 records of properties in the database, 
I should get all 5 properties in a list 
"""
def test_all(db_connection): 
    db_connection.seed("seeds/backend_seed.sql")
    repository = PropertiesRepository(db_connection)
    actual = repository.all()
    expected = [
        Properties(1, 'Flat', 'Sunny 2bdr flat in city centre', 100, 'Hackney', '2023-08-30', '2023-12-31', True, 1),
        Properties(2, 'Maisonette','Large 3bdr 2ba with spacious garden', 300, 'Brixton', '2023-08-30', '2023-12-31', True, 2),
        Properties(3, 'Annex','Double bed 2floor with ensuite', 80, 'Brighton', '2023-08-30', '2023-12-31', True, 3)
    ]
    
    print("Actual properties:")
    for prop in actual:
        print(prop)

    print("Expected properties:")
    for prop in expected:
        print(prop)
        
    assert expected[0].property_type == actual[0].property_type
    assert actual == expected 

# """
# Given a properties id, 
# I should get a properties corresponding to that id  
# """
# def test_find(db_connection):
#     db_connection.seed("seeds/backend_seed.sql")
#     repository = PropertiesRepository(db_connection)
#     actual = repository.find(1)
#     expected = Properties(1, 'Nineteen Eighty-Four', 'George Orwell')
#     assert actual == expected


# """
# Given a properties instance, 
# I should be able to insert that properties into the properties table 
# """
# def test_create(db_connection):
#     db_connection.seed("seeds/backend_seed.sql")
#     repository = PropertiesRepository(db_connection)
#     properties = Properties(None, "Harry Potter", "J.K")
#     repository.create(properties)
#     actual = repository.all()
#     expected = [
#         Properties(1, 'Nineteen Eighty-Four', 'George Orwell'),
#         Properties(2, 'Mrs Dalloway', 'Virginia Woolf'),
#         Properties(3, 'Emma', 'Jane Austen'),
#         Properties(4, 'Dracula', 'Bram Stoker'),
#         Properties(5, 'The Age of Innocence', 'Edith Wharton'), 
#         Properties(6, "Harry Potter", "J.K")

#     ]
#     assert actual == expected 


# """
# Given a properties instance, 
# I should be able to update that properties in the properties table
# """

# def test_update(db_connection):
#     db_connection.seed("seeds/backend_seed.sql")
#     repository = PropertiesRepository(db_connection)
#     properties = (Properties(1, "Nineteen Eighty-nine", "George Orwell"))
#     repository.update(properties)
#     assert repository.find(1) == Properties(1, 'Nineteen Eighty-nine', 'George Orwell')
    
# # delete a properties 

# def test_delete(db_connection):
#     db_connection.seed("seeds/backend_seed.sql")
#     repository = PropertiesRepository(db_connection)
#     repository.delete(1)
#     assert repository.all() == [
#         Properties(2, 'Mrs Dalloway', 'Virginia Woolf'),
#         Properties(3, 'Emma', 'Jane Austen'),
#         Properties(4, 'Dracula', 'Bram Stoker'),
#         Properties(5, 'The Age of Innocence', 'Edith Wharton')

#     ]
