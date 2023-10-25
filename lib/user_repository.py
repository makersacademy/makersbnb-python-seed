from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        return [User(row['id'], row['username'], row['email'], row['password'])
                for row in rows]
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                                [user.username, user.email, user.password])
        
    def get_user_by_id(self, user_id):
        rows = self._connection.execute('SELECT id, username, email FROM users WHERE id = %s',[user_id])
        row = rows[0]
        return User(row['id'], row['username'], row['email'], None)

