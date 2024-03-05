class Space:
    def __init__(self, id, name, location, description, price, owner):
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.price = price
        self.owner = owner

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Property name: {self.name}. Location: {self.location}. Property Description: {self.description}. Price per night: £{self.price}. Owner name and contact: {self.owner}."
    
# maybe something about available dates here? or do we have a separate class for the dates that connects to this class?