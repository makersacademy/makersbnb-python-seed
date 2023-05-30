from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row['actualname'], row["password"], row["email"])
            users.append(item)
        return users
    
    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (username, actualname, password, email) VALUES (%s, %s, %s, %s)', 
            [user.username, user.actualname, user.password, user.email]
        )
        return None
    # def create(self, listing):
    #     self._connection.execute(
    #     'INSERT INTO listings (name, description, price, user_id) VALUES (%s, %s, %s, %s)', 
    #     [listing.name, listing.description, listing.price, listing.user_id]
    # )
#         self._connection.execute('INSERT INTO users (title, author_name) VALUES (%s, %s)', [                           book.title, book.author_name])
#         return None
    

