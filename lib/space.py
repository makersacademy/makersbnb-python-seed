"""Table: spaces
id: SERIAL
space_name: text
description: text
price: money
dates_booked: date[]
dates_available: date[]
user_id: int"""


class Space:
    def __init__(self, id, space_name, description, price, user_id, start_date, end_date):
        self.id = id
        self.space_name = space_name
        self.description = description
        self.price = price
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space ({self.id} {self.user_id} {self.space_name} {self.description} {self.price} {self.start_date} {self.end_date})"
    
    
