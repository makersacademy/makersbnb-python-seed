from lib.database_connection import *
from lib.space import Space

class SpaceRepository:
    def __init__(self,dbconnection):
        self._connection = dbconnection

    def create_space(self, space):
        self._connection.execute('INSERT INTO spaces (name, description, price, ownerid) VALUES (%s, %s, %s,%s)', [
        space.name, space.description, space.price, space.ownerid])
        return None
    
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row['price'], row['owner_id'] ) 
            spaces.append(item)
        return spaces

    def find(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row['price'], row['owner_id'] ) 

    def delete(self, space_id):
        self._connection.execute(
            'DELETE FROM space WHERE id = %s', [space_id])
        return None