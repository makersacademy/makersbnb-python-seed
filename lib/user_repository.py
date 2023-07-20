from lib.user import *
from flask import session

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["user_password"], row["email"])
            users.append(item)
        return users
    def create(self, user):
        rows = self._connection.execute(
            'INSERT INTO users (username, user_password, email) VALUES (%s, %s, %s) RETURNING id', [
                user.username, user.user_password, user.email])
        user.id = rows[0]['id']

    def find_user(self, email):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [email])
        if rows == []:
            return "Invalid email"
        row = rows[0]
        return User(row["id"], row["username"], row["user_password"], row["email"])
    
    def username_and_password_match_user(self, email, password):
        rows = self._connection.execute(
            'SELECT user_password from users WHERE email = %s', [email])
        if not rows:
            return False
        row = rows[0]
        if row['user_password'] == password:
            session['email'] = email
            return True
        else: 
            return False

