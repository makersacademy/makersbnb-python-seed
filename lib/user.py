class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    def is_valid(self):
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False
        return True