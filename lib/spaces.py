"""
ID - Integer
Name - String
Description  String
Price - Float
Host_ID - Integer
"""

class Space:
    def __init__(self, id, name, description, price, host_ID):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.host_ID = host_ID

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
 
    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.price}, {self.host_ID})"
    
    def is_valid(self):
        if self.name == None or self.name.strip() == '':
            return False
        if self.description == None or self.description.strip() == '':
            return False
        if self.price == None:
            return False
        if self.host_ID == None:
            return False
        return True
        
    def generate_errors(self):
        errors = []
        if self.name == None or self.name == '':
            errors.append("Name can't be blank")
        
        if self.description == None or self.description == '':
            errors.append("Description can't be blank")

        if self.price == None or str(self.price) == '':
            errors.append("Price can't be blank")
        
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)