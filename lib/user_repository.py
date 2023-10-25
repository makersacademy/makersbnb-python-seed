from lib.user import User
import hashlib

class UserRepository():

    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row["id"], row["email"], row["password"])
            users.append(user)
        return users
    
    def create(self, email, password):
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()
        self._connection.execute(
            'INSERT INTO users (email, password) VALUES (%s, %s)',
            [email, hashed_password])

    def check_password(self, email, password_attempt):
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])
        return len(rows) > 0

    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        user = User(rows[0]['id'], rows[0]['email'], rows[0]['password'])
        return user
