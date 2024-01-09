from dataclasses import dataclass
from lib.database_connection import DatabaseConnection
import hashlib
import re

@dataclass
class User:
    id: int
    username: str
    email: str
    password: str
    bookings: list = None

    def is_valid(self):
        if '' in [self.username, self.email, self.password]:
            return False
        if not re.match(r'^\w+$', self.username):
            return False
        if not re.match(r'^\w+(\.\w+)*@\w+(\.[a-z]+)+$', self.email):
            return False
        return True


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
        binary_password = user.password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()
        rows = self._connection.execute(
            "INSERT INTO users (username, email, password, bookings) " \
            "VALUES (%s, %s, %s, %s) RETURNING id", 
            [user.username, user.email, hashed_password, user.bookings]
        )
        return rows[0]['id']

    def find_user_by_username(self, username):
        rows = self._connection.execute("SELECT * FROM users WHERE username = %s", [username])
        row = rows[0]
        return User(row['id'], row['username'], row['email'], row['password'], row['bookings'])

    def add_booking(self, booking):
        user = self.find_user_by_id(booking.user_id)
        bookings = user.bookings
        if bookings == None:
            bookings = [booking.id]
        else:
            bookings.append(booking.id)
        self._connection.execute("UPDATE users SET bookings = %s WHERE id = %s", [bookings, user.id])

    def check_user(self, user):
        """Check if a user exists by their username and email."""
        errors =[]
        all_users = self.get_all_users()
        usernames = [user.username for user in all_users]
        emails = [user.email for user in all_users]
        if user.username in usernames:
            errors.append(f'username: {user.username} is already in use')
        if user.email in emails:
            errors.append(f"email: '{user.email}' is already registered.")
        return errors
    
    def check_password_correct(self, username, password_attempt):
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()
        rows = self._connection.execute(
            'SELECT * FROM users WHERE username = %s AND password = %s',
            [username, hashed_password_attempt])
        return len(rows) > 0
