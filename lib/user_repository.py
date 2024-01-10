from lib.user import User
import hashlib
import os


def hash_pass(password):
    h = hashlib.sha256(password.encode())
    return h.hexdigest()


def is_valid(password):
    if password is not None:
        valid_length = len(password) >= 8
        has_special_char = any(char in "!@#$%?" for char in password)
        has_digit = any(char.isdigit() for char in password)
        return valid_length and has_special_char and has_digit


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, email, password):
        hashed_password = hash_pass(password)
        try:
            self._connection.execute(
                "INSERT into users (username, email, password) VALUES (%s, %s, %s)",
                [username, email, hashed_password],
            )
            return True
        except Exception as e:
            print("Error creating user: ", e)
            return False

    def all(self):
        rows = self._connection.execute(
            "SELECT username, email, password FROM users"  # security issue with calling password?
        )
        return [User(row["username"], row["email"], row["password"]) for row in rows]

    def find_user_by_username(self, username):
        rows = self._connection.execute(
            "SELECT username, email, password FROM users WHERE username = %s",
            [username],
        )
        if rows:
            user = rows[0]
            return User(user["username"], user["email"], user["password"])
        return None

    def password_hash():
        pass

    def login(self, username, password):
        rows = self._connection.execute(
            "SELECT username, email, password FROM users WHERE username = %s",
            [username],
        )
        if rows:
            user = rows[0]
            # retrieve stored password
            stored_password = user["password"]
            # hash the inputted password and create
            hashed_password = hash_pass(password)
            print(f"stored_password: {stored_password}")
            print(f"hashed_password: {hashed_password}")

            # compare the hashed pword with the stored password
            if stored_password == hashed_password:
                return True
            else:
                print("Failed to login: Please check details")
                return None
        else:
            print("User not found")
            return None

    def request_space():
        pass
