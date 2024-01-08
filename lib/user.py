class User:
    def __init__(self, id, firstName, lastName, email, password):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.firstName}, {self.lastName}, {self.email}, {self.password})"
    
    def is_valid(self):
        # if self.firstName == None or self.firstName == "" or self.lastName == None or self.lastName == "":
        #     return False
        # elif '@' not in self.email or '.' not in self.email or self.email == "" or self.email == None:
        #     return False
        if any(char.isdigit() for char in self.password) == False:
            return False

        return True
    
    def generate_errors(self):
        errors = []
        
        if any(char.isdigit() for char in self.password) == False:
            errors.append("Password has to be atleast 8 characters and contain atleast 1 number")
        
        if len(errors)==0:
            return None
        else:
            return ", ".join(errors)

    