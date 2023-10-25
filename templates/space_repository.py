from lib.space import Space

class SpaceRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = [Space(row['name'], row['description'], row['size'], row['price'], row['owner_id'], row['id']) for row in rows]

        return spaces
    
    def find(self, space_id):
        rows = self._connection.execute(f'SELECT * FROM spaces WHERE id = {space_id}')
        spaces = [Space(row['name'], row['description'], row['size'], row['price'], row['owner_id']) for row in rows]
        
        return spaces[0] if spaces else None
    
    def create(self, space):
        return self._connection.execute(f"INSERT INTO spaces(name, description, size, price, owner_id) VALUES('{space.name}', '{space.description}', {space.size}, {space.price}, {space.owner_id}) RETURNING id")[0]
    
    def delete(self, space_id):
        self._connection.execute(f'DELETE FROM spaces WHERE id = {space_id}')