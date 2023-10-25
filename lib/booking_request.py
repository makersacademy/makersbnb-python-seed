class BookingRequest:
    def __init__(self, user_id, space_id, booking_request_date, booking_request_status):
        self.user_id = user_id
        self.space_id = space_id
        self.booking_request_date = booking_request_date
        self.booking_request_status = booking_request_status
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.user_id}, {self.space_id}, {self.booking_request_date}, {self.booking_request_status}"
        