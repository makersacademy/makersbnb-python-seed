import re

class User:
    def __init__(self, id, email, first_name, last_name, phone_number, password):
        self.id = id
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.phone_number = phone_number.replace(' ','')
        self.password = password    

    def password_validator(self):
        password_rule = "r'^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9]).{8,}$'"
        match_result = re.match(password_rule,self.password)
        if match_result is None:
            raise InvalidPassword('Password not OK')
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.first_name}, {self.last_name}, {self.phone_number}, {self.password})"
    

class InvalidPassword(Exception):
    pass