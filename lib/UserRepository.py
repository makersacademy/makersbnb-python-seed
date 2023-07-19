
from lib.User import *

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * from users")
        return [User(row["id"], row["email"], row ["password"]) 
        for row in rows
        ]
    
    def find(self, id):
        rows = self.connection.execute(
         'SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["email"], row["password"])

    
    def create(self, user):
        self.connection.execute("INSERT INTO users (email, password) VALUES (%s, %s)", [user.email, user.password])
        return True
    
    def find_user_by_email(self,user_email):
        email_rows = self.connection.execute(
         'SELECT * from users WHERE email = %s', [user_email])
        if len(email_rows) > 0:
            return "User already exists"
        elif email_rows == []:
            return True







    

