class Space:
    def __init__(self, id, description, price, user_id, name):
        self.id = id
        self.description = description
        self.price = price
        self.user_id = user_id
        self.name = name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Space({self.id}, {self.description}, {self.price}, {self.user_id}, {self.name})'

