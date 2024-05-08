class User:
    def __init__(self,id,email,password):
        self.id = id
        self.email = email
        self.password = password
        
    def __eq__(self,other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.password})"
    
    def generate_errors(self):
        errors = []
        if self.email == None or self.email == "":
            errors.append("email can't be blank!")
        if self.password == None or self.password == "":
            errors.append("Password can't be blank!")
        if len(self.password) < 8:
            errors.append("Passwords must be 8 characters or longer!")
        if not any(char in self.password for char in ['!', '@', '$', '%', '&']):
                errors.append("Passwords must include one of the following special characters(! @ $ % &)")
        if not any(char.isupper() == True for char in self.password):
            errors.append("Passwords must include a Capital Letter!") 
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        
    def is_valid(self):
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False
        if len(self.password) < 8:
            return False
        if not any(char in self.password for char in ['!', '@', '$', '%', '&']):
            return False
        if not any(char.isupper() == True for char in self.password):
            return False
        return True

    
        



