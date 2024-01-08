from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        
        return [
            User(row['id'], row['email'], row['passw'])
            for row in rows
        ]