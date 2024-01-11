from lib.user import User
import hashlib

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
        

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row['id'], row['user_name'], row['email'], row['password'])
            users.append(user)
        return users
    
    def create(self, user):
          rows = self._connection.execute('INSERT INTO users (user_name, email, password) VALUES (%s, %s, %s) RETURNING id', [
              user.user_name, user.email, user.password])
          row = rows[0]
          user.id = row['id']
          return None

    
    def find(self, email, password_attempt):
        binary_password = password_attempt.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()

        rows = self._connection.execute('SELECT email, password FROM users WHERE email = %s AND password = %s', [email, hashed_password])
        return len(rows) > 0
    
    def get_username_by_id(self, id):
        rows = self._connection.execute("SELECT user_name FROM users WHERE id = %s", [id])
        row = rows[0]
        username = row['user_name']
            
        return username
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])
        if rows: 
            row = rows[0]
            return User(row["id"], row["user_name"], row["email"], row["password"])
        else: 
            return None
    

    def find_by_name(self, name):
        rows = self._connection.execute('SELECT * FROM users WHERE user_name = %s', [name])

        if rows:
            row = rows[0]
            return User(row["id"], row["user_name"], row["email"], row["password"])
        else:
            # Return None if the user is not found
            return None
    
    
    def find_by_email(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        row = rows[0]
        return User(row["id"], row["user_name"], row["email"], row["password"])
    