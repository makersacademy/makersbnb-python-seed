class Space():
    def __init__(self, id, name, description, price, user_id, dates = None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
        self.dates = dates or []

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price}, {self.user_id})"
    

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    