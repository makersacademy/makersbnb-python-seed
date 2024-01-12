class User:
    def __init__(self,id,first_name, last_name, email, telephone_number, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.telephone_number = telephone_number
        self.password = password
    
    def __eq__(self,other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email}, {self.telephone_number}, {self.password})"