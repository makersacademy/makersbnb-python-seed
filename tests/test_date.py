from lib.date import *
from datetime import datetime

def test_date_init():
    date = Date(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1)
    assert date.date == datetime(2023, 1, 1, 0, 0)
    assert date.listing_id

def test_listing_eq():
    listing1 = Date(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1)
    listing2 = Date(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1)
    assert listing1 == listing2

def test_listing_repr():
    listing = Date(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1)
    assert str(listing) == "LISTING 1 date: 01/01/2023"