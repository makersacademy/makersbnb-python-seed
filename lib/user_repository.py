from lib.user import User


class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    # def all(self):
    #     rows = self._connection.execute('SELECT * from artists')
    #     artists = []
    #     for row in rows:
    #         item = Artist(row["id"], row["artist_name"], row["genre"])
    #         artists.append(item)
    #     return artists

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            user = User(row['id'], row['name'], row['email'], row['password'])
            users.append(user)
        return users

    def find(self, name, password):
        record = self._connection.execute('SELECT EXISTS (SELECT * FROM users WHERE name = %s AND password = %s)', (name, password))
        return record[0].get('exists')

    def create(self, user):
        results = self._connection.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id', [user.name, user.email, user.password])
        result = results[0]
        user.id = result['id']
        return user


    # def update(self, user):
    #     self._connection.execute('UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s', [user.name, user.email, user.password, user.id])

    # def delete(self, id):
    #     self._connection.execute('DELETE FROM users WHERE id = %s', [id])

