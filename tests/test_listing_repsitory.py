from lib.listing_repository import ListingRepository
from lib.listing import Listing
from lib.database_connection import DatabaseConnection

# all() method returns a list of all Listings for given user_id

def test_all_returns_all_listings(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    result = repository.all()
    assert result == [
                    Listing(1, 'first-test-listing', 'Description 1', 45, 1),
                    Listing(2, 'second-test-listing', 'Description 2', 70, 1),
                    Listing(3, 'third-test-listing', 'Description 3', 35, 2),
                    Listing(4, 'fourth-test-listing', 'Description 4', 50, 3),
                    Listing(5, 'fifth-test-listing', 'Description 5', 100, 2),
                    Listing(6, 'sixth-test-listing', 'Description 6', 85, 1)]

# find_by_user() lists all listings associated with given user_id
def test_find_by_user_returns_given_users_listings(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    result = repository.find_by_user(3)
    assert result == [Listing(4, 'fourth-test-listing', 'Description 4', 50, 3)]

# create() adds a new listed to the database 
def test_create_adds_new_listing(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    repository.create(None, 'seventh-test-listing', 'Description 7', 38, 3)
    result = repository.all()
    assert result == [
                    Listing(1, 'first-test-listing', 'Description 1', 45, 1),
                    Listing(2, 'second-test-listing', 'Description 2', 70, 1),
                    Listing(3, 'third-test-listing', 'Description 3', 35, 2),
                    Listing(4, 'fourth-test-listing', 'Description 4', 50, 3),
                    Listing(5, 'fifth-test-listing', 'Description 5', 100, 2),
                    Listing(6, 'sixth-test-listing', 'Description 6', 85, 1),
                    Listing(7, 'seventh-test-listing', 'Description 7', 38, 3)]
    
# delete() removes a listed space from the database
def tests_delete_removes_listing_from_db(db_connection):
    db_connection.seed('seeds/makers_bnb.sql')
    repository = ListingRepository(db_connection)
    repository.delete(6)
    result = repository.all()
    assert result == [
                    Listing(1, 'first-test-listing', 'Description 1', 45, 1),
                    Listing(2, 'second-test-listing', 'Description 2', 70, 1),
                    Listing(3, 'third-test-listing', 'Description 3', 35, 2),
                    Listing(4, 'fourth-test-listing', 'Description 4', 50, 3),
                    Listing(5, 'fifth-test-listing', 'Description 5', 100, 2)]