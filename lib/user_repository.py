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
    
    def create(self, user):
        email=user.email
        password=user.password
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        # Store the email and hashed password in the database
        self._connection.execute(
            'INSERT INTO users (email, password) VALUES (%s, %s)',
            [email, hashed_password])



