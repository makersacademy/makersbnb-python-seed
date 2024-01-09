from lib.user import User

class UserRepository:
    def __init__(self,connection):
        self._connection = connection

    
    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row['id'], row['first_name'], row['last_name'], row['email'], row['telephone_number'], row['password'])
            users.append(item)
        return users
    
    def create(self,user):
        rows = self._connection.execute(
            'INSERT INTO users (first_name, last_name, email, telephone_number, password) VALUES (%s,%s,%s,%s,%s) RETURNING ID',[
                user.first_name, user.last_name, user.email, user.telephone_number, user.password
            ]
        )
        row = rows[0]
        user.id = row['id']
        return user

    def find_user(self,user_id):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE id = %s',[user_id])
        row = rows[0]
        return User(row['id'], row['first_name'], row['last_name'], row['email'], row['telephone_number'], row['password'])
    
    def find_by_email(self, email):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s', [email]
        )
        if rows:
            row = rows[0]
            return User(
                id=row['id'],
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                telephone_number=row['telephone_number'],
                password=row['password']
            )
        else:
            return None