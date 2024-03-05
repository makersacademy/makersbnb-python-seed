from lib.space_repository import *
from lib.space import *

#When we call SpacesRepository#all
#We get a list of spaces objects reflecting the seed data.

def test_get_all_records_from_spaces(db_connection): 
    db_connection.seed("seeds/makersbnb.sql") 
    repository = SpaceRepository(db_connection)
    result = repository.all()
    assert result == [
        Space(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob'),
        Space(2, 'Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim'),
        Space(3, 'Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane'),
        Space(4, 'Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan'),
        Space(5, 'Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil')
    ]

def test_find_single_property_by_location(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    space = repository.find_by_location('Brighton')
    assert space == Space(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')

def test_find_single_property_by_name(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    space = repository.find_by_property_name('Bob House')
    assert space == Space(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')

# def test_find_single_property_by_column(db_connection):
#     db_connection.seed("seeds/makersbnb.sql")
#     repository = SpaceRepository(db_connection)
#     space = repository.find_by_column_name('location', 'Brighton')
#     assert space == Space(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob')

def test_create_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(6, 'Mati House', 'Scarborough', '1 bedroom, 1 bathroom, Modern Property', 200, 'Mati'))

    result = repository.all()
    assert result == [
        Space(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 300, 'Bob'),
        Space(2, 'Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim'),
        Space(3, 'Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane'),
        Space(4, 'Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan'),
        Space(5, 'Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil'),
        Space(6, 'Mati House', 'Scarborough', '1 bedroom, 1 bathroom, Modern Property', 200, 'Mati'),
    ]

def test_delete_space(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.delete('Bob House') # Deletes Bob's House
    
    result = repository.all()
    assert result == [
        Space(2, 'Jim House', 'London', '3 bedrooms, 3 bathrooms, Modern property', 350, 'Jim'),
        Space(3, 'Jane House', 'Newcastle', '4 bedrooms, 2 bathrooms, Georgian-era property', 450, 'Jane'),
        Space(4, 'Megan House', 'Exmouth', '5 bedrooms, 5 bathrooms, Contemporary property', 600, 'Megan'),
        Space(5, 'Phil House', 'Manchester', '2 bedrooms, 1 bathrooms, Barn-style property', 200, 'Phil')
    ]

def test_update_space_price(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)
    repository.update_price(350, 'Bob House') # Update price Bob's House
    result = repository.find_by_property_name("Bob House")
    assert result == Space(1, 'Bob House', 'Brighton', '3 bedrooms, 2 bathrooms, Victorian-era property', 350, 'Bob')