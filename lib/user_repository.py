from lib.user import User

class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["user_name"], row["user_password"])
            users.append(item)
        return users

    # Find a single user by its id
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["user_name"], row["user_password"])

    # Create a new user
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, user):
        self._connection.execute('INSERT INTO users (user_name, user_password) VALUES (%s, %s)', [
                                 user.username, user.password])
        return None

    # Delete user by its id
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None