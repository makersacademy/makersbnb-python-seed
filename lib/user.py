# from lib.user_repository import UserRepository

class User():
    def __init__(self, id, username, user_password, email):
        self.id = id
        self.username = username
        self.user_password = user_password
        self.email = email

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.user_password}, {self.email})"
    
    def is_valid_username(self):
        if self.username == None or self.username == "":
            return False
        return True

    def is_valid_user_password(self):
        if len(self.user_password) < 8:
            return False
        return True
    
    def generate_errors(self):
        errors = []
        if not self.is_valid_username():
            errors.append("Username can't be blank")
        if not self.is_valid_user_password():
            errors.append("Password must be at least 8 latters")
        if len(errors) == 0:
            return None
        return errors
    
    