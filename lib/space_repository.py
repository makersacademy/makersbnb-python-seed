from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        list_to_return = []
        for row in rows:
            space = Space(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
            list_to_return.append(space)
        if len(list_to_return):
            return list_to_return
        
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id=%s", [id])
        if rows:
            row = rows[0]
        space = Space(row['id'], row['name'], row['descr'], row['price'], row['user_id'])
        return space
    
    def update(self, space:Space):
        self._connection.execute("UPDATE spaces SET name=%s, descr=%s, price=%s WHERE id=%s", [space.name, space.desc, space.price, space.id])