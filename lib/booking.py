from datetime import date

class Booking:
    def __init__(self, id, space_id, booker_id, start_date, end_date, confirmed):
        self.id = id
        self.space_id = space_id
        self.booker_id = booker_id
        self.start_date = start_date
        self.end_date = end_date
        self.confirmed = confirmed
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.space_id}, {self.booker_id}, {self.start_date}, {self.end_date}, {self.confirmed})"
