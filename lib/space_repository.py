from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row['name'], row['location'], row['price'], row['size'], row['description'])
            spaces.append(item)
        return spaces
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["location"], row["price"], row["size"], row["description"])