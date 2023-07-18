from lib.request import Request

def test_constructs_with_fields():
    request = Request(1, 1, 1, "18/07/23")
    assert request.id == 1
    assert request.user_id == 1
    assert request.space_id == 1
    assert request.date_to_book == "18/07/23"

def test_equality():
    request1 = Request(1, 1, 1, "18/07/23")
    request2 = Request(1, 1, 1, "18/07/23")
    assert request1 == request2

def test_formatting():
    request = Request(1, 1, 1, "18/07/23")
    assert str(request) == "Request(1, 1, 1, 18/07/23)"