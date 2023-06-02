class Booking:
    def __init__(self, id, requester_id, listing_id, booking_date, approved):
        self.id = id
        self.requester_id = requester_id
        self.listing_id = listing_id
        self.booking_date = booking_date
        self.approved = approved

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"booking({self.id}, {self.requester_id}, {self.listing_id}, {self.booking_date}, {self.approved})"
    
    def approve_booking(self):
        self.approved = True
