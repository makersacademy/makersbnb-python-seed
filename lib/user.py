from flask_login import UserMixin
import hashlib

class User(UserMixin):
    def __init__(self, id, user_name, email, password):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        binary_password = password.encode("utf-8")
        return hashlib.sha256(binary_password).hexdigest()

    def check_password(self, password_attempt):
        hashed_password_attempt = self._hash_password(password_attempt)
        return hashed_password_attempt == self.password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.user_name}, {self.user_name}, {self.password})"