class Listing:
    def __init__(self, id, name, description, price, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"listing({self.id}, {self.name}, {self.description}, {self.price}, {self.user_id})"
