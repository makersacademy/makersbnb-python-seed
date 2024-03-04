from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection