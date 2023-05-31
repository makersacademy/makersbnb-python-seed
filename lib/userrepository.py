from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self.connection = connection

    def get(self):
        results = self.connection.execute('SELECT * FROM users')
        userlist = []
        for result in results:
            this = User(result['id'], result['email'], result['password'])
            userlist.append(this)
        return userlist
    
    def create(self, user):
        get_back_id = self.connection.execute(f"INSERT INTO users (email, password) VALUES ('{user.email}', '{user.password}') RETURNING ID;")
        user.id = get_back_id[0]["id"]