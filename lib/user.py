class User:
    def __init__(self, email_address, username, password):
        self.email_address = email_address
        self.username = username
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
