from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, email, password):
        self._connection.execute(
            "INSERT into users (username, email, password) VALUES (%s, %s, %s)",
            [username, email, password],
        )

    def all(self):
        rows = self._connection.execute(
            "SELECT username, email, password FROM users"
        )
        return [
            User(row["username"], row["email"], row["password"])
            for row in rows
        ]

    def password_hash():
        pass

    def login():
        pass

    def logout():
        pass

    def request_space():
        pass
