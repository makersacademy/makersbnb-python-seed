class User:
    def __init__(self, id, email):
        self.id = id
        self.email = email

    def __repr__(self):
        return f"user({self.id}, '{self.email}')"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__