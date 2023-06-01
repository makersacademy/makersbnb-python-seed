class User:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, username, actualname, email, password):
        self.id = id
        self.username = username
        self.actualname = actualname
        self.email = email
        self.password = password

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.actualname}, {self.email}, {self.password})"
