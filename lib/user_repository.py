from lib.user import User

class UserRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        return [User(row["id"], row["name"], row["username"], row["email"], row["password"]) for row in rows]
    
    def add(self, user):
        self._connection.execute(
            "INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)",
            [user.name, user.username, user.email, user.password],
        )
        return None
    
    def get_by_username(self, username):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        row = rows[0]
        return User(row[0], row[1], row[2], row[3], row[4])
    
    def get_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s", [email])
        row = rows[0]
        return User(row[0], row[1], row[2], row[3], row[4])