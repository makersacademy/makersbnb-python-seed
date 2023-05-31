from lib.user import User
import hashlib

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row['actualname'], row["email"],  row["password"])
            users.append(item)
        return users
    
    def create(self, user):
        # binary_password = user.password.encode("utf-8")
        # hashed_password = hashlib.sha256(binary_password).hexdigest()
        self._connection.execute(
            'INSERT INTO users (username, actualname, email, password) VALUES (%s, %s, %s, %s)', 
            [user.username, user.actualname, user.email, user.password]
        )
        return None
    
    # def check_password(self, username, password_attempt):
    #     binary_password_attempt = password_attempt.encode("utf-8")
    #     hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
    #     print(hashed_password_attempt)
    #     # Check whether there is a user in the database with the given email
    #     # and a matching password hash, using a SELECT statement.
    #     rows = self._connection.execute(
    #         'SELECT password FROM users WHERE username = %s AND password = %s',
    #         [username, hashed_password_attempt])
    #     print(rows)
    #     return len(rows) > 0
    def check_password(self, username, password_attempt):
        # binary_password_attempt = password_attempt.encode("utf-8")
        # hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
        # print(hashed_password_attempt)
        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE username = %s AND password = %s',
            [username, password_attempt])
        print(rows)
        return len(rows) > 0
    



