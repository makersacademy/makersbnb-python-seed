from lib.listing_repo import *
from lib.listing import *

def test_listing_repo_all(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = ListingRepo(db_connection)
    assert repo.all() == [
        Listing('Cozy Cottage', 'A charming cottage for a peaceful retreat', 99.99, 1),
        Listing('Beachfront Villa', 'Enjoy stunning ocean views in this luxury villa', 249.95, 2),
        Listing('Mountain Chalet', 'Experience the beauty of the mountains in this cozy chalet', 149.99, 3),
        Listing('City Apartment', 'Convenient urban living in the heart of the city', 89.49, 4),
        Listing('Lakefront Cabin', 'Rustic cabin on the tranquil shores of the lake', 124.50, 5), 
        Listing('Seaside Bungalow', 'Relax in a charming bungalow by the sea', 199.99, 6),
        Listing('Luxury Resort Suite', 'Indulge in luxury at this 5-star resort suite', 499.95, 7),
        Listing('Countryside Retreat', 'Escape to the peaceful countryside in this cottage', 79.99, 8),
        Listing('Historic Mansion', 'Step back in time at this historic mansion', 349.99, 9),
        Listing('Riverside Cabin', 'Cozy cabin with a river view, perfect for fishing', 109.75, 10)
    ]

def test_listing_repo_find_with_listing_id(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = ListingRepo(db_connection)
    assert repo.find_with_listing_id(1) == Listing('Cozy Cottage', 'A charming cottage for a peaceful retreat', 99.99, 1)

def test_listing_add(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = ListingRepo(db_connection)
    repo.add('test name', 'test desc', 1.99, 1) 
    assert repo.all()[-1] == Listing('test name', 'test desc', 1.99, 1)
