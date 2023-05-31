from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection
# Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
                item = User(row["id"], row["name"], row["email"], row["password"])
                users.append(item)
        return users
  # Create a new user
  # Do you want to get its id back? Look into RETURNING id;
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', [
        user.name, user.email, user.password])
        return None
 # Find a single user by their id
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["password"])
