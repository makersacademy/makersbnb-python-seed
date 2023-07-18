from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["user_password"], row["email"])
            users.append(item)
        return users
    def create(self, user):
        rows = self._connection.execute(
            'INSERT INTO users (username, user_password, email) VALUES (%s, %s, %s) RETURNING id', [
                user.username, user.user_password, user.email])
        user.id = rows[0]['id']
