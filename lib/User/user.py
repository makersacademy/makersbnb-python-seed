from uuid import uuid4
from hashlib import sha256

class User:
    def __init__(self, username, email, phone_number, password):
        self.id = str(uuid4())
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password_hash = self.set_password_hash(password)
            
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def set_password_hash(self, password):
        hash_algorithm = sha256()
        hash_algorithm.update(password.encode("utf-8"))
        return hash_algorithm.hexdigest() 