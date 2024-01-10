class Booking:
    def __init__(self, id, date, space_id, guest_id, confirmed):
        self.id = id
        self.date = date
        self.space_id = space_id
        self.guest_id = guest_id
        self.confirmed = confirmed

    def __repr__(self):
        return f"Booking({self.id}, {self.date}, {self.space_id}, {self.guest_id}, {self.confirmed})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__