class UserRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def check_exists(self, username):
        users = self._connection.execute(
            'SELECT * FROM users WHERE username=%s', [username]
        )
        
        if len(users) == 0:
            return False
        else: 
            return True
        