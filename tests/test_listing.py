from lib.listing import Listing

'''
Listing constructed with id, name, description, price_per_night, available_from, and available_to
'''
def test_listing_constructs():
    listing = Listing(1, "testname", "testdescription", 100, "2021-01-01", "2021-01-02")
    assert listing.id == 1
    assert listing.name == "testname"
    assert listing.description == "testdescription"
    assert listing.price_per_night == 100
    assert listing.available_from == "2021-01-01"
    assert listing.available_to == "2021-01-02"

'''
Formatting to string
'''
def test_listing_formats_to_string_correctly():
    listing = Listing(1, "testname", "testdescription", 100, "2021-01-01", "2021-01-02")
    assert str(listing) == "Listing:(1, testname, testdescription, 100, 2021-01-01, 2021-01-02)"

'''
Check to see two identical listings are equal
'''
def test_listings_are_equal():
    listing1 = Listing(1, "testname", "testdescription", 100, "2021-01-01", "2021-01-02")
    listing2 = Listing(1, "testname", "testdescription", 100, "2021-01-01", "2021-01-02")
    assert listing1 == listing2