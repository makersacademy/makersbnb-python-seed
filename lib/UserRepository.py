
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
    
    def find_by_email(self, email):
        rows = self.connection.execute(
         'SELECT * from users WHERE email = %s', [email])
        if rows == []:
            return User(None,"","")
        row = rows[0]
        return User(row["id"], row["email"], row["password"])

    
    def create(self, user):
        self.connection.execute("INSERT INTO users (email, password) VALUES (%s, %s)", [user.email, user.password])
        return None
    





    

