from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"])
            users.append(item)
        return users
    
    def find(self, user_email):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [user_email])
        row = rows[0]
        return User(row["id"], row["first_name"], row["last_name"], row["email"], row["password"])
    
    def accountExists (self, userEmail):
        rows = self._connection.execute(
            'SELECT * from users WHERE email = %s', [userEmail])
        if len(rows) == 0:
            return False
        
        return True
    
    def create(self, user):
        rows = self._connection.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s) RETURNING id', [
                                    user.firstName, user.lastName, user.email, user.password])
        row = rows[0]
        user.id = row["id"]
        return user

    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None 