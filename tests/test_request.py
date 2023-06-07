from lib.request import Request
"""
Test that a request is well initialized
"""
def test_request_construction():
    request = Request(3, 1, 2, 1, "2023-06-12", False)
    assert request.id == 3
    assert request.owner_id == 1
    assert request.visitor_id == 2
    assert request.space_id == 1 
    assert request.request_date == "2023-06-12"
    assert request.confirmed == False

def test_requests_are_equal():
    request1 = Request(3, 1, 2, 1, "2023-06-12", False)
    request2 = Request(3, 1, 2, 1, "2023-06-12", False)
    assert request1 == request2

def test_requests_format_nicely():
    request = Request(3, 1, 2, 1, "2023-06-12", False)
    assert str(request) == "Request(3, 1, 2, 1, 2023-06-12, False)"