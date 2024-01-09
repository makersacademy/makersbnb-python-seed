"""Table: spaces
id: SERIAL
space_name: text
description: text
price: money
dates_booked: date[]
dates_available: date[]
user_id: int"""


class Space:
    def __init__(self, id, space_name, description, price, user_id):
        self.id = id
        self.space_name = space_name
        self.description = description
        self.price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
