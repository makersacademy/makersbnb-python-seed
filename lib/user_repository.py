from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
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