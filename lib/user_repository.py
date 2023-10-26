from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users(username, email, password) VALUES (%s, %s, %s)",
            [user.username, user.email, user.password]
        )
        return None

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], ["email"], ["password"])
            users.append(item)
            return users
