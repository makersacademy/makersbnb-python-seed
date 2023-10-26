class Space:

    def __init__(self, id, name, description, price, date_from, date_to, user_id):

        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.date_from = date_from
        self.date_to = date_to
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def nice_format(self):
        return f"{self.name}, {self.description}, {self.price}, {self.date_from}, {self.date_to}, {self.user_id}"