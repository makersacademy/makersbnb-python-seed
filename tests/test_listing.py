from lib.listing import *

def test_listing_init():
    listing = Listing(1, 'test name', 'test desc', 1.99, 1)
    assert listing.id == 1
    assert listing.listing_name == 'test name'
    assert listing.listing_description == 'test desc'
    assert listing.listing_price == 1.99
    assert listing.user_id == 1

def test_listing_eq():
    listing1 = Listing(1, 'test name', 'test desc', 1.99, 1)
    listing2 = Listing(1, 'test name', 'test desc', 1.99, 1)
    assert listing1 == listing2

def test_listing_repr():
    listing = Listing(1, 'test name', 'test desc', 1.99, 1)
    assert str(listing) == "LISTING 1 name: test name - desc: test desc - price: 1.99 - user_id: 1"