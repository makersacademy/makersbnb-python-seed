from lib.space import Space

class SpaceRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = [Space(row['id'], row['name'], row['description'], row['size'], row['price'], row['owner_id']) for row in rows]

        return spaces
    
    def find(self, space_id):
        rows = self._connection.execute(f'SELECT * FROM spaces WHERE id = {space_id}')
        spaces = [Space(row['id'], row['name'], row['description'], row['size'], row['price'], row['owner_id']) for row in rows]
        
        return spaces[0] if spaces else None
    
    def create(self, space):
        self._connection.seed('seeds/airbnb.sql')
        rows = self._connection.execute(
            "INSERT INTO spaces (name, description, size, price, owner_id) VALUES (%s, %s, %s, %s, %s) RETURNING id", 
            [space.name, space.description, int(space.size), int(space.price), space.owner_id]
        )
        space.id = rows[0]['id']
        return None
    
    def delete(self, space_id):
        self._connection.execute(f'DELETE FROM spaces WHERE id = {space_id}')


    def get_rented_spaces(self, user):
        query = '''
        SELECT s.id, s.name, s.description, s.size, s.price, s.owner_id
        FROM spaces s
        INNER JOIN bookings b ON s.id = b.space_id
        AND b.booker_id = %s
        '''
        params = (user.id,)
        rows = self._connection.execute(query, params)
        rented_spaces = [Space(row['id'], row['name'], row['description'], row['size'], row['price'], row['owner_id']) for row in rows]
        return rented_spaces
