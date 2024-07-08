from lib.BookingRequest import BookingRequest

"""
Simple property constructs with an id etc.
"""
def test_property_request_constructs():
    propReq = BookingRequest('08-Jul-2024', '09-Jul-2024', 1, 1)
    assert propReq.property_id == 1
    assert propReq.customer_id == 1
    assert propReq.status == 'PENDING'
    
"""
Call the state change methods.
"""
def test_property_request_constructs():
    propReq = BookingRequest('08-Jul-2024', '09-Jul-2024', 1, 1)
    assert propReq.property_id == 1
    assert propReq.customer_id == 1
    # TODO : Change above.