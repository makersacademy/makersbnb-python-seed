class Space:
    def __init__(self, id, title, description, price, date_range, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.date_range = date_range
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Space({self.id}, {self.title}, {self.description}, {self.price}, {self.date_range}, {self.user_id})"