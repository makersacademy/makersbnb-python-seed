from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection


    def find(self, user_id):
        rows = self._connection.execute('SELECT * from users WHERE id =%s', [user_id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"], row["password"])
        


    def create(self, user):
        self._connection.execute('INSERT INTO users(name, email, password) VALUES (%s, %s, %s)' 
                    [user.name, user.email, user.password])
        return None


