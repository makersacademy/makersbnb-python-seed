class Booking:
    def __init__(self, id, start_date, end_date, property_id, user_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.property_id = property_id
        self.user_id = user_id

    def __repr__(self):
        return f"Booking({self.id}, {self.start_date}, {self.end_date}, {self.property_id}, {self.user_id})"