class Listing:
    def __init__(self, id, name, description, price_per_night, available_from, available_to):
        self.id = id
        self.name = name
        self.description = description
        self.price_per_night = price_per_night
        self.available_from = available_from
        self.available_to = available_to

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Listing:({self.id}, {self.name}, {self.description}, {self.price_per_night}, {self.available_from}, {self.available_to})"