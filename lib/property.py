class Property:
    def __init__(self, name, description, price, owner, booked_status):
        self.name = name
        self.description = description
        self.price = price 
        self.owner = owner #possibly user_id
        self.booked_status = booked_status
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.name}\n {self.description}\n £{self.price}\n Owner: {self.owner}"
        
        
        