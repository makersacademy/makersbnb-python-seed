from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["email"], row["password"])
            users.append(item)
        return users
    
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id', [user.email, user.password])
        row = rows[0]
        user.id = row["id"]
        return user