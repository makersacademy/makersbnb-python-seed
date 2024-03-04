class Space:
    def __init__(self, id, name, description, price, owner):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.owner = owner

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Property name: {self.name}. /n
        Property Description: {self.description}. /n
        Price per night: {self.price}. /n 
        Owner name and contact: {self.owner}."
    
# maybe something about available dates here? or do we have a separate class for the dates that connects to this class?