from lib.space import Space
from lib.database_connection import DatabaseConnection

class SpaceRepository:
    def __init__(self, connection):
        self._conn = connection
    
    def find(self, id):
        row = self._conn.execute(f"SELECT * FROM spaces WHERE id={id}")
        row = row[0]
        space = Space(row['id'], row['name'], row['desc'], row['price'])
        return space