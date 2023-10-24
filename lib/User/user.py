class User:
    def __init__(self, username, email, phone_number, password):
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password_hash = self.set_password_hash(password)
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def set_password_hash(self, password):
        return hash(password)