class Space:
    def __init__(self, id, space_name, description, price_per_night, user_id, start_date, end_date):
        self.id = id
        self.space_name = space_name
        self.description = description
        self.price_per_night = price_per_night
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}, {self.space_name}, {self.description}, {self.price_per_night}, {self.user_id}, {self.start_date}, {self.end_date}"
