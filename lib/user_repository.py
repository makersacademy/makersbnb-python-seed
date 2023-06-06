from lib.user import User
class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            users.append(User(row['id'], row['first_name'],
                            row['last_name'], row['email'], row['password']))
        return users
    
    def create_user(self, user):
        self._connection.execute('INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)', [user.first_name, user.last_name, user.email, user.password])

    def check_password(self, email, password):
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, password])

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0
    
    def find_user_by_email(self, email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        print("HEREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
        print(rows)
        row = rows[0]
        return User(row['id'], row['first_name'], row['last_name'], row['email'], row['password'])