import re
import pytest

class User:
    def __init__(self, username, password):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
            raise ValueError("Invalid username format, enter your email address")
        self.username = username

        special_characters = '!@$%&'
        if len(password) <= 7 or all(char not in password for char in special_characters):
            raise ValueError("Password does not meet the criteria, password needs to be 8 characters long and contain special character")
        self.password = password

