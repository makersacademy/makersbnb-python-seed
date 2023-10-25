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
        if self.firstName == None or self.firstName == "" or self.lastName == None or self.lastName == "":
            return False
        elif '@' not in self.email or '.' not in self.email or self.email == "" or self.email == None:
            return False
        elif len(self.password) < 8 or (any(char.isdigit() for char in self.password)) == False or self.password == "" or self.password == None:
            return False

        return True
    
    def generate_errors(self):
        errors = []
        if self.firstName == None or self.firstName == "" or self.lastName == None or self.lastName == "":
            errors.append("Name cannot be blank")
        if '@' not in self.email or '.' not in self.email:
            errors.append("Invalid email")
        if len(self.password) < 8 or (any(char.isdigit() for char in self.password)) == False:
            errors.append("Password has to be atleast 8 characters and contain atleast 1 number")
        
        if len(errors)==0:
            return None
        else:
            return ", ".join(errors)

    