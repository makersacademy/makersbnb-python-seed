from lib.user import User

class UserRepository():

    def __init__(self,connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row["id"], row["email"], row["password"])
            users.append(user)
        return users
    
    def create(self, user):
        self.connection.execute('INSERT INTO users (email, password) VALUES(%s, %s)', 
                                [user.email, user.password])
