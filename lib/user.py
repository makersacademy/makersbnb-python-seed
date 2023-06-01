import re

class User:
    def __init__(self, id, name, email, password):
        # We initialise with all of our attributes
        # Each column in the table should have an attribute here
        self.id = id
        self.name = name
        self.email = email
        self.password = password
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.email}, {self.password})"
    
    def is_valid(self):
        if re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", self.email) == None:
            return False
        
        if len(self.password) < 4 or re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{4,}$", self.password) == None:
            return False
        
        if self.name == None or self.name == "":
            return False
        
        return True
    
    def generate_errors(self):
        errors = []
        if self.email == None or self.email == "":
            errors.append("Email can't be blank")
        elif re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", self.email) == None:
            errors.append("Invalid email")
        
        if self.password == None or self.password == "":
            errors.append("Password can't be blank")
        elif len(self.password) < 4:
            errors.append("Password must be at least 4 characters long")
        
        if  re.search(r'\d', self.password) == None:
            errors.append("Password must contain a number")

        if re.search(r'\w*[A-Z]\w*', self.password) == None:
            errors.append("Password must contain at least 1 uppercase letter")

        if len(self.password) > 0 and re.search("\\W+", self.password) == None:
                errors.append("Password must have at least 1 special character")

        if self.name == None or self.name == "":
            errors.append("Name can't be blank")

        if len(errors) > 0:
            return ", ".join(errors)
        else:
            return None
