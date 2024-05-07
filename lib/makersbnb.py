class MakersBnb():
    def __init__(self,id, email, password):
        self.id = id
        self.email = email
        self.password = password
        
    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Album
    def __repr__(self):
        return f"users({self.id}, {self.email}, {self.password}"


