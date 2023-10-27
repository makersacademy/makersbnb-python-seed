from lib.request import *
from datetime import datetime


def test_request_init():
    request = Request(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1, 1, 1)
    assert request.date == datetime(2023, 1, 1, 0, 0)
    assert request.listing_id == 1
    assert request.requested_by_id == 1
    assert request.requested_from_id == 1

def test_request_eq():
    request1 = Request(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1, 1, 1)
    request2 = Request(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1, 1, 1)
    assert request1 == request2

def test_request_repr():
    request = Request(datetime.strptime('2023-01-01', '%Y-%m-%d'), 1, 1, 1)
    assert str(request) == "Request(date: 01/01/2023 - listing: 1 - requested_by: 1 - requested_from: 1)"