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
        return User[row["id"], row["username"]]
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (username) VALUES (%s)', [user.username])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM users WHERE id = %s', [id])
        return None