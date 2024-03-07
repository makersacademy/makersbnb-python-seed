import re

class User:
    def __init__(self, id, username, password):
        self.id = id
        
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
            raise ValueError("Invalid username format, enter your email address")
        self.user_name = username

        special_characters = '!@$%&'
        if len(password) <= 7 or all(char not in password for char in special_characters):
            raise ValueError("Password does not meet the criteria, password needs to be 8 characters long and contain a special character")
        self.user_password = password

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"User({self.id}, {self.user_name}, {self.user_password}"