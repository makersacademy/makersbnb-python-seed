class Booking:
    def __init__(self, id, date_id, user_id ):
        self.id = id
        self.date_id = date_id
        self.user_id = user_id
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.date_id}, {self.user_id})"