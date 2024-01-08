class Space:
    def __init__(self, id, address, name, price, description, date_added, image, availability):
        self.id = id
        self.address = address
        self.name = name 
        self.price = price
        self.description = description
        self.date_added = date_added
        self.image = image
        self.availability = availability
    
    def __eq__(self, other):
        return __dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.address}, {self.name}, {self.price}, {self.description}, {self.date_added}, {self.image}, {self.availability})"