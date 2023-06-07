class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.password})"
    
    def is_valid(self):
        if self.first_name == None or self.first_name == "":
            return False
        if self.last_name == None or self.last_name == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if self.first_name == None or self.first_name == "":
            errors.append("First Name can't be blank")
        if self.last_name == None or self.last_name == "":
            errors.append("Last Name can't be blank")
        if self.email == None or self.email == "":
            errors.append("Email can't be blank")
        if self.password == None or self.password == "":
            errors.append("Password can't be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)