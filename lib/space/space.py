from uuid import uuid4

class Space():

    def __init__(self, name, owner_id, description, price, start_date, end_date):
        self.id = str(uuid4())
        self.name = name
        self.owner_id = owner_id
        self.description = description
        self.price = price
        self.start_date = start_date
        self.end_date = end_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__