from lib.user import User

class UserRepository:

# initializing a database connection
    def __init__(self, connection):
        self._connection = connection

# get a listing of all the users registered on MakersBnB
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["password"])
            users.append(item)
        return users

# create a new user on MakersBnB
### COME BACK AND CORRECT SQL value for users?

    def create(self, user):
        self._connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [
            user.username, user.password])
        return None

