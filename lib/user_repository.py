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
        
    def create(self, user):
        
        self._connection.execute(
            "INSERT INTO users (email, passw) VALUES (%s, %s)",
            [user.email, user.passw]
        )
        
    def check_valid_signup(self, username):
        datalist = self.all()
        for user in datalist:
            if username == user.email:
                return False
        return True

    def check_valid_login(self,email,passw):
        datalist = self.all()
        for user in datalist:
            if email == user.email and passw == user.passw:
                return True
        return False