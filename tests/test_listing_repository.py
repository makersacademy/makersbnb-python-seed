from lib.listings import *
from lib.listing_repository import *

def test_get_all_listings(db_connection):
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = ListingRepository(db_connection) # Create a new ListingRepository

    listings = repository.all() # Get all listings

    # Assert on the results
    assert listings == [
        Listing(1, "Charming Cottage", "A small, cozy cottage in the woods.", 100.00, 1),
        Listing(2, "City Apartment", "An apartment in the heart of the city.", 150.00, 2),
        Listing(3, "Beach House", "A house with a beautiful ocean view.", 200.00, 3),
    ]

def test_create_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)

    repository.create(Listing(None, "Mountain Cabin", "A cozy cabin in the mountains.", 125.00, 1))

    result = repository.all()
    assert result == [
        Listing(1, "Charming Cottage", "A small, cozy cottage in the woods.", 100.00, 1),
        Listing(2, "City Apartment", "An apartment in the heart of the city.", 150.00, 2),
        Listing(3, "Beach House", "A house with a beautiful ocean view.", 200.00, 3),
        Listing(4, "Mountain Cabin", "A cozy cabin in the mountains.", 125.00, 1),
    ]


def test_get_single_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = ListingRepository(db_connection)

    listing, available_dates = repository.get_single_listing(1)

    assert listing == Listing(1,'Charming Cottage', 'A small, cozy cottage in the woods.', 100.00, 1)
    assert available_dates == ['2023-06-05','2023-06-06','2023-06-07']
        
