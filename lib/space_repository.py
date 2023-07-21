from lib.space import *

class SpaceRepository():
    def __init__(self, connection):
        self._connect = connection

    def all(self):
        rows = self._connect.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], 
                        row["name"], 
                        row["description"], 
                        row["price"], 
                        row["availability"], 
                        row["user_id"])
            spaces.append(item)
        return spaces
    
    def create(self, space):
        rows = self._connect.execute('INSERT INTO spaces (name, description, price, availability, user_id) VALUES (%s,%s,%s,%s,%s) RETURNING id',[space.name, space.description, space.price, space.availability, space.user_id])
        row = rows[0]
        space.id = row["id"]
        return None
    
    def find(self, id):
        rows = self._connect.execute('SELECT * FROM spaces WHERE spaces.id = %s', [id])
        space = []
        for row in rows:
            item = Space(row["id"], 
                        row["name"], 
                        row["description"], 
                        row["price"], 
                        row["availability"], 
                        row["user_id"])
            space.append(item)
        return space
    
    def update_availability(self, space_id, new_availability):
        self._connect.execute('UPDATE spaces SET availability = %s WHERE id = %s', [new_availability, space_id])