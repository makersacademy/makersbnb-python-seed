import re

class User:
    def __init__(self, id, email, first_name, last_name, phone_num, password):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_num = phone_num
        self.password = password    

    def password_validator(self):
        password_rule = "r'^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.*[0-9]).{8,}$'"
        try:
            re.match(password_rule,self.password)
            return
        except Exception:
            return "Password not OK"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.email}, {self.first_name}, {self.last_name}, {self.phone_num}, {self.password})"