from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users ORDER BY id')
        users = []
        for row in rows:
            user = User(row['id'], row['email'], row['username'], row['password'])
            users.append(user)
        return users
    
    def create(self, user):
        self.connection.execute(
            'INSERT INTO users (email, username, password) VALUES (%s, %s, %s)',
            [user.email, user.username, user.password]
        )
        return None
    
    def find(self, id):
        rows = self.connection.execute(
            'SELECT * FROM users WHERE id = %s', [id]
        )
        row = rows[0]
        return User(row['id'], row['email'], row['username'], row['password'])
    
    def update(self, user):
        self.connection.execute(
            'UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s',
            [user.email, user.username, user.password, user.id])
        return None
    
    def delete(self, user_id):
        self.connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id]
        )
        return None