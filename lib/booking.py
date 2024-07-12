class Booking:

    def __init__(self, id, listing_id, booked_at, booker_id, check_in, check_out):
        self.id = id
        self.listing_id = listing_id
        self.booked_at = booked_at
        self.booker_id = booker_id
        self.check_in = check_in
        self.check_out = check_out

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking:({self.id}, {self.listing_id}, {self.booked_at}, {self.booker_id}, {self.check_in}, {self.check_out})"