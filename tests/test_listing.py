from lib.listings import *



# 
def test_listing_constructs():
    listing = Listing(1, "Test listingname", "Test description", 100.99, 1)
    assert listing.id == 1
    assert listing.name == "Test listingname"
    assert listing.description == "Test description"
    assert listing.price == 100.99
    assert listing.user_id == 1

# """
# We can format listings to strings nicely
# # """
def test_listings_format_nicely():
    listing = Listing(1, "Test listingname", "Test description", 100.99, 1)
    assert str(listing) == "listing(1, Test listingname, Test description, 100.99, 1)"
#     # Try commenting out the `__repr__` method in lib/listing.py
#     # And see what happens when you run this test again.

# # """
# # We can compare two identical listings
# # And have them be equal
# # """
def test_listings_are_equal():
    listing1 = Listing(1, "Test listingname", "Test description", 100.99, 1)
    listing2 = Listing(1, "Test listingname", "Test description", 100.99, 1)
    assert listing1 == listing2