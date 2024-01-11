class Booking:
    def __init__(self, id, space_id, user_id, date, price):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.date = date
        self.price = price

    def __repr__(self):
        return f"Space({self.id}, {self.space_id}, {self.user_id}, {self.date}, {self.price})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__