
class Properties:
    def __init__(self, id, property_type, description, price, location, start_date, end_date, available, user_id):
        self.id = id
        self.property_type = property_type
        self.description = description
        self.price = price
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.available = available
        self.user_id = user_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.property_type} - {self.description} - {self.price} - {self.location} - {self.start_date} - {self.end_date} - {self.available} - {self.user_id}"
    
