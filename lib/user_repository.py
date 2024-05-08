from lib.user import *
class UserRepository:
    def __init__(self, connection):
        self.connection = connection
        self.users = []

    def find_by_id(self,id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s',[id])
        if rows:
            row = rows[0]
            return User(row['id'], row['email'],row['password'])
        else:
            raise Exception("User not found!")


    def create(self, user):
        rows = self.connection.execute('INSERT INTO users (email, password) Values(%s, %s) RETURNING id',[user.email, user.password])
        row = rows[0]
        user.id = row['id']
        return user


    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        user_list = []
        for row in rows:
            current_user = User(row['id'],row['email'],row['password'])
            user_list.append(current_user)
        return user_list


