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
        cursor = self.connection.cursor()
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            user = User(result[0], result[1], result[2], result[3], result[4])
            return user
        return None
    
    def get_by_email(self, email):
        cursor = self.connection.cursor()
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            user = User(result[0], result[1], result[2], result[3], result[4])
            return user
        return None