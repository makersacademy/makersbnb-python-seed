from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Space(row['id'], row['name'], row['price'], row['description'], row['user_id'])
            spaces.append(item)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row['id'], row['name'], row['price'], row['description'], row['user_id'])
    
    def create(self, name, price, description, user_id):
        self._connection.execute('INSERT INTO spaces (name, price, description, user_id) VALUES (%s, %s, %s, %s)', [name, price, description, user_id])

    def update(self, space):
        self._connection.execute('UPDATE spaces SET name = %s, price = %s, description = %s, user_id = %s WHERE id = %s', [space.name, space.price, space.description, space.user_id, space.id])
        
    def delete(self, id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [id])

    def find_user_spaces(self, user_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE user_id = %s', [user_id])
        spaces = []
        for row in rows:
            item = Space(row['id'], row['name'], row['price'], row['description'], row['user_id'])
            spaces.append(item)
        return spaces

    def get_space_name(self, space_id):
        query = "SELECT name FROM spaces WHERE id = %s"
        rows = self._connection.execute(query, [space_id])
        space_names = []
        for row in rows:
            item = row['name']
            space_names.append(item)
        return space_names
