from dataclasses import dataclass
from lib.database_connection import DatabaseConnection

@dataclass
class User:
    id: int
    username: str
    email: str
    password: str
    bookings: list = None


class UserRepo:
    def __init__(self, connection):
        self._connection = connection

    def get_all_users(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = User(row['id'], row['username'], row['email'], row['password'], row['bookings'])
            users.append(user)
        return users
    
    def find_user_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])
        row = rows[0]
        return User(row['id'], row['username'], row['email'], row['password'], row['bookings'])
    
    def create_user(self, user):
        rows = self._connection.execute(
            "INSERT INTO users (username, email, password, bookings) " \
            "VALUES (%s, %s, %s, %s) RETURNING id", 
            [user.username, user.email, user.password, user.bookings]
        )
        return rows[0]['id']