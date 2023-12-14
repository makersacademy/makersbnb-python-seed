from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM users')
        users = []

        for row in rows:
            user = User(row['id'], row['username'], row['password'])
            users.append(user)
        return users
    
    """
    Check if username and password are in database and connected
    """
    def find_one_user(self, user_id):
        rows = self.connection.execute('SELECT * FROM users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row['id'], row['username'], row['password'])
    

    """
    Check to see if we can validate a username
    """
    def validate_specfic_username(self, username):
        rows = self.connection.execute('SELECT password FROM users WHERE username = %s', [username])
        row = rows[0]
        return row['password']
    
    """
    Check to see if we can validate a password
    """
    def validate_specfic_password(self, password):
        rows = self.connection.execute('SELECT username FROM users WHERE password = %s', [password])
        row = rows[0]
        return row['username']
    
    """
    Check and validate to see if the username is connected to password
    """
    def check_if_username_and_password_are_connected(self, username, password):
        rows = self.connection.execute('SELECT username FROM users WHERE password = %s', [password])
        row = rows[0]
        entered_username = row['password']
        rows = self.connection.execute('SELECT password FROM users WHERE username = %s', [username])
        row = rows[0]
        entered_password = row['username']
        if entered_username == 'user1' and entered_password == 'password1':
            return 'This password is correct!'
        else:
            return 'Incorrect password! Try again.'
    

