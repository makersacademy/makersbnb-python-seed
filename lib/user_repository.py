from lib.user import User
class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        return [User(row["id"], row["username"]) for row in rows]
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["username"], row["password"])
    
    # Find a single user by its username and password
    def find_by_username_and_password(self, username, password):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s AND password = %s', [username, password])
        if len(rows) == 0:
            return None
        row = rows[0]
        return User(row["id"], row["username"], row["password"])
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [user.username, user.password])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None