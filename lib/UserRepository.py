from lib.User import User

class UserRepostiroy:
    def __init__(self,connection):
        self.connection = connection
    def all(self):
        rows = self.connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row['id'], row['username'], row['password'])
            users.append(item)
        return users
    
    def create_user(self, user):
        self.connection.execute('INSERT INTO users (username, password) VALUES (%s, %s)', [user.username, user.password])
        return None                