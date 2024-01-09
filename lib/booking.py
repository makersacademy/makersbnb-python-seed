class Booking():
    def __init__(self, id, user_id, date_booked):
        self.id = id
        self.user_id = user_id
        self.date_booked = date_booked

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.user_id}, {self.date_booked})"
    
    