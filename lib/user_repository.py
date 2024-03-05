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


    def find(self, name, password):
        record = self._connection.execute('SELECT EXISTS (SELECT * FROM users WHERE name = %s AND password = %s)', (name, password))
        return record[0].get('exists')



