class Booking:
    def __init__(self, id, date, status, space_id, guest_id):
        self.id = id
        self.date = date
        self.status = status
        self.space_id = space_id
        self.guest_id = guest_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.date}, {self.status}, {self.space_id}, {self.guest_id})"
    
     