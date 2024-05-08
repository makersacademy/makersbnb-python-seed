from lib.space import *

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price"], row["user_id"])
            spaces.append(item)
        return spaces
    
    def find(self, space_id):
        row = self._connection.execute('SELECT * from spaces WHERE id = %s', (space_id,))
        return Space(row[0]["id"], row[0]["name"], row[0]["description"], row[0]["price"], row[0]["user_id"])
    
    def create(self, name, description, price, user_id):
        self._connection.execute('INSERT INTO spaces (name, description, price, user_id) VALUES (%s, %s, %s, %s)', (name, description, price, user_id))
        return None
    
    def delete(self, space_id):
        self._connection.execute('DELETE from spaces WHERE id = %s', (space_id,))
        return None
    