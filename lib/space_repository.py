from lib.space import Space
from lib.database_connection import DatabaseConnection

class SpaceRepository:
    def __init__(self, connection):
        self._conn = connection
    
    def find(self, id):
        row = self._conn.execute(f"SELECT * FROM spaces WHERE id={id}")
        row = row[0]
        space = Space(row['id'], row['name'], row['description'], row['price'])
        return space
    
    def update(self, space:Space):
        self._conn.execute("UPDATE spaces SET name=%s, description=%s, price=%s WHERE id=%s", (space.name, space.desc, space.price, space.id))