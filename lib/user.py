class User():
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__