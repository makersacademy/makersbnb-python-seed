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
        
        get_user_id = self._connection.execute(
            "INSERT INTO users (email, passw) VALUES (%s, %s) RETURNING id",
            [user.email, user.passw]
        )
        user_id = get_user_id[0]['id']
        return user_id
        
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
                return self._get_user_id(email)
        return False
    
    def _get_user_id(self,email):
        rows = self._connection.execute('SELECT * FROM users WHERE email = %s',[email])
        for row in rows:
            return row['id']