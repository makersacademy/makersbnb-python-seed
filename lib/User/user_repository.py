class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def check(self, username):
        users = self._connection.execute(
            'SELECT * FROM users WHERE username=%s', [username]
        )
        
        if len(users) == 0:
            return False
        else: 
            return True
    
    def create(self, user):
        self._connection.execute(
            "INSERT INTO users " +
            "(username, email, passwordhash, phonenumber) " + 
            "VALUES (%s, %s, %s, %s)", [user.username, user.email, user.password_hash, user.phone_number]
        )
