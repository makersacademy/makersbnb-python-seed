class Space:
    def __init__(self, id, name, location, price, size, description):
        self.id = id
        self.name = name
        self.location = location
        self.price = price
        self.size = size
        self.description = description

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.location}, {self.price}, {self.size}, {self.description})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__