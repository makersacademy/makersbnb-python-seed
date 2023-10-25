from lib.booking_request import *

class BookingRequestRepository:
    def __init__(self, connection):
        self._connection = connection 
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM booking_requests")
        booking_requests = []
        for row in rows:
            booking_request = BookingRequest(row["user_id"], row["space_id"], row["booking_request_date"], row["booking_request_status"])
            booking_requests.append(booking_request)
        return booking_requests


    def find(self, user_id):
        rows = self._connection.execute("SELECT * FROM booking_requests WHERE user_id = %s", [user_id])
        row = rows [0]
        booking_request = BookingRequest(row["user_id"], row["space_id"], row["booking_request_date"], row["booking_request_status"])
        return booking_request
    
    
    def create(self, new_booking_request):
        self._connection.execute("INSERT INTO booking_requests (user_id, space_id, booking_request_date, booking_request_status) VALUES (%s, %s, %s, %s)",
                            [new_booking_request.user_id, new_booking_request.space_id, new_booking_request.booking_request_date, new_booking_request.booking_request_status])