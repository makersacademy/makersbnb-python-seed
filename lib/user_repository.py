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
        return User(row['id'], row['name'], row['username'], row['email'], row['password'])
    
    def get_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
        row = rows[0]
        return User(row['id'], row['name'], row['username'], row['email'], row['password'])
    
    # Check if username is already in the users table
    def username_is_unique(self, username):
        # Count the number of times the username is in the database
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        result = self._connection.execute(query, [username])
        count = result[0]['count']
        return count == 0

    # Check if email is already in the users table
    def email_is_unique(self, email):
        # Count the number of times the email is in the database
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        result = self._connection.execute(query, [email])
        count = result[0]['count']
        return count == 0
    
    # Check that password is correct for the username
    def check_password(self, email, password):
        query = "SELECT password FROM users WHERE email = %s"
        result = self._connection.execute(query, [email])
        user_password = result[0]['password']
        return password == user_password