
class Property:
    
    def __init__(self,id,name,description,price,user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
            return f"Property({self.id},{self.name},{self.description},{self.price:.2f},{self.user_id})"
    

    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.description == None or self.description == "":
            return False
        if self.price == None or self.price == "":
            return False
        if self.user_id == None or self.user_id == "":
            return False
        return True
    

    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("Name can't be blank")
        if self.description == None or self.description == "":
            errors.append("Description can't be blank")
        if self.price == None or self.price == "":
            errors.append("Price can't be blank")
        if self.user_id == None or self.user_id == "":
            errors.append("User ID can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)

