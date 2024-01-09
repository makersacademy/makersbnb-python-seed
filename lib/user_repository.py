from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
        

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row['id'], row['user_name'], row['email'], row['password'])
            users.append(user)
        return users
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (user_name, email, password) VALUES (%s, %s, %s)', [
            user.user_name, user.email, user.password])
        return None
    
    def find(self, email, password_attempt):
        rows = self._connection.execute('SELECT email, password FROM users WHERE email = %s AND password = %s', [email, password_attempt])
        return len(rows) > 0