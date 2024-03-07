class BookingRequest:
    def __init__(self, id, booking_id, request_status):
        self.id = id
        self.booking_id = booking_id
        self.request_status = request_status
        

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.booking_id}, {self.request_status}"
    
     