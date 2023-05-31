class Booking:
    def __init__(self, id, user_id, listing_id, booking_date):
        self.id = id
        self.user_id = user_id
        self.listing_id = listing_id
        self.booking_date = booking_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"booking({self.id}, {self.user_id}, {self.listing_id}, {self.booking_date})"
