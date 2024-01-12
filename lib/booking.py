import datetime

class Booking():
    def __init__(self, id, date, confirmed, rejected, user_id, space_id):
        self.id = id
        self.date = date
        self.confirmed = confirmed
        self.rejected = rejected
        self.user_id = user_id
        self.space_id = space_id
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.date}, {self.confirmed}, {self.rejected}, {self.user_id}, {self.space_id})"
    
