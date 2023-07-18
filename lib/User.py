class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"user({self.id}, {self.email}, {self.password})"
    
    def is_valid(self):
        if self.email == None or self.email== "":
            return False
        if self.password == None or self.password== "":
            return False
        return True
    
    def raise_errors(self):
        errors = []
        if self.email == None or self.email== "":
            errors.append("fill in email")
        if self.password == None or self.password== "":
            errors.append("fill in password")
        if len(errors) == 0:
            return None 
        else:
            return ", ".join(errors)
