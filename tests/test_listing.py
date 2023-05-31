from lib.listing import Listing


"""
Listing constructs with a price, location, availability, description and user_id
"""
def test_listing_constructs():
    listing = Listing(1, 1, 150, 'name', "listing description")
    assert listing.id == 1
    assert listing.user_id == 1
    assert listing.price == 150
    assert listing.name == 'name'
    assert listing.description == "listing description"

"""
We can format listings to strings nicely
"""
def test_listings_format_nicely():
    listing = listing = Listing(1, 1, 150, 'name', "listing description")
    assert str(listing) == "Listing(id=1, user_id=1, price=150, name='name', description='listing description')"

"""
We can compare two identical listings
And have them be equal
"""
def test_listings_are_equal():
    listing_1 = Listing(1, 1, 150, 'name', "listing description")
    listing_2 = Listing(1, 1, 150, 'name', "listing description")
    assert listing_1 == listing_2
