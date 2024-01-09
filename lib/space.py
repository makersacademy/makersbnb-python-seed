class Space:
    def __init__(self, id, address, name, price, image_path, description, date_added, date_available, user_id):
        self.id = id
        self.address = address
        self.name = name 
        self.price = price
        self.image_path = image_path
        self.description = description
        self.date_added = date_added
        self.date_available = date_available
        self.user_id = user_id
        
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.address}, {self.name}, {self.price}, {self.image_path}, {self.description}, {self.date_added}, {self.date_available}, {self.user_id})"
    
