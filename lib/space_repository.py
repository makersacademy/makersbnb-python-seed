from lib.space import Space

class SpaceRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            spaces.append(Space(row['id'], row['space_name'], row['description'], row['price_per_night'], row['user_id']))
        return spaces
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        row = rows[0]
        space = Space(row['id'], row['space_name'], row['description'], row['price_per_night'], row['user_id'])
        return space
    
    def create(self, space):
        self._connection.execute('INSERT INTO spaces \
                                (space_name, description, price_per_night, user_id) \
                                VALUES (%s, %s, %s, %s)', \
                                [space.space_name, space.description, space.price_per_night, space.user_id])
        return None
    
    def delete(self, space_id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [space_id])
        return None