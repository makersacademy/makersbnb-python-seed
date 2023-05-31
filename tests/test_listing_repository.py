from lib.listing import Listing
from lib.listing_repository import ListingRepository

def test_db_list_all_listings(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = ListingRepository(db_connection)

    result = repository.all()
    assert result == [
        Listing(1, 1, 150, 'name', "listing description"),
        Listing(2, 1, 300, 'name', "listing description")
    ]