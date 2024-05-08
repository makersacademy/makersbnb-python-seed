from lib.spaces import *


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], 
                        row["owner"], 
                        row["name"], 
                        row["description"], 
                        row["price_per_night"], 
                        row["active"])
            spaces.append(item)
        return spaces

    def create(self, space):
        self._connection.execute('INSERT INTO spaces(owner, name, description, price_per_night, active) VALUES (%s, %s, %s, %s, %s)', [space.owner, space.name, space.description, space.price_per_night, space.active])
        return None 
    
    def find(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], 
                        row["owner"], 
                        row["name"], 
                        row["description"], 
                        row["price_per_night"], 
                        row["active"])
    
    def delete(self, user_id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [user_id])
        return None 