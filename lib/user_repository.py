from lib.user import User
from flask import flash

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
        
    def get_user_by_username(self, username):
        rows = self._connection.execute('SELECT id, username, email, password FROM users WHERE username = %s',[username])
        if len(rows) == 0:
            flash('Invalid username or password', 'error')
        else:
            row = rows[0]
            return User(row['id'], row['username'], row['email'], row['password'])
    

