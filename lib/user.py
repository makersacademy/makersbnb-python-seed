from flask_login import UserMixin
import hashlib

class User(UserMixin):
    def __init__(self, id, user_name, email, password):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password = password
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.user_name}, {self.email}, {self.password})"       
