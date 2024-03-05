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
    

    def find_by_location(self, space_location):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE location = %s', [space_location])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["description"], row["price"], row["owner"])


    def find_by_property_name(self, property_name):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE name = %s', [property_name])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["description"], row["price"], row["owner"])


    # def find_by_column_name(self, column_name, search):
    #     rows = self._connection.execute(
    #         'SELECT * from spaces WHERE %s = %s', [column_name, search])
    #     row = rows[0]
    #     return Space(row["id"], row["name"], row["location"], row["description"], row["price"], row["owner"])
    

    def delete(self, space_name):
        self._connection.execute(
            'DELETE FROM spaces WHERE name = %s', [space_name])
        return None


    def update_price(self, new_price, name):
        self._connection.execute(
            'UPDATE spaces SET price = %s WHERE name = %s', [new_price, name])
        return None

    #class to return available dates? Or have them pick any date, and then returns if that date is available or not?