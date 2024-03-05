from lib.space import Space
from lib.database_connection import *

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            space = Space(
                row['id'],
                row['name'],
                row['location'], 
                row['description'], 
                row['price'],
                row['owner'])
            spaces.append(space)
        return spaces
    

    def create(self, space):
        self._connection.execute('INSERT INTO spaces (id, name, location, description, price, owner) VALUES (%s, %s, %s, %s, %s, %s)', [
                                space.id, space.name, space.location, space.description, space.price, space.owner])
        return None
    

    def find(self, space_location):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE location = %s', [space_location])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["description"], row["price"], row["owner"])
    
    def delete(self, space_name):
        self._connection.execute(
            'DELETE FROM spaces WHERE name = %s', [space_name])
        return None

    #class to return available dates? Or have them pick any date, and then returns if that date is available or not?