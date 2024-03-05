from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = User(row["id"], row["email"])
            users.append(user)
        return users
    
    def create_new_user():
        pass

    def log_user_in():
        pass