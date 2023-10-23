# File: lib/user_repository.py
from lib.user import User

class UserRepository:

    def __init__(self, connection) -> None:
        self._connection = connection


    def all(self):
        """retreive all albums"""

        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = User(row['username'], row['spaces'])
            users.append(user)
        return users
    

    def find(self, user_id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        row = rows[0]
        user = User(row['username'], row['spaces'])
        return user


    def create(self, new_user):
        self._connection.execute('INSERT INTO users (username, spaces) VALUES (%s, %s)',
                                [new_user.username, new_user.spaces])
        