from lib.property import Property
from lib.property_repository import PropertyRepository
from lib.database_connection import DatabaseConnection


def test_all_return_list_of_properties(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = PropertyRepository(db_connection)

    assert repository.all() == [
        Property(1,'Hackers Hideaway', 'A mystery place full of bugs', 50.00, 1),
        Property(2,'Ma house', 'Its a very nice', 25.5, 1),
        Property(3,'Makers HQ', 'Cosy and helpful', 100.00, 4)
    ]

def test_create_property(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = PropertyRepository(db_connection)

    repository.create(Property(None,"NameTest","DescriptionTest",99.00,1))

    assert repository.all() == [
        Property(1,'Hackers Hideaway', 'A mystery place full of bugs', 50.00, 1),
        Property(2,'Ma house', 'Its a very nice', 25.5, 1),
        Property(3,'Makers HQ', 'Cosy and helpful', 100.00, 4),
        Property(4,"NameTest","DescriptionTest",99.00,1)
    ]

def test_find_property(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository = PropertyRepository(db_connection)
    assert repository.find(1) == Property(1,'Hackers Hideaway', 'A mystery place full of bugs', 50.00, 1)

def test_price_formatter_formats_to_2_decimals(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repository =  PropertyRepository(db_connection)
    property = repository.find(2)
    formatted_price = repository.price_formatter(property)
    assert formatted_price == "£25.50 per night"
    