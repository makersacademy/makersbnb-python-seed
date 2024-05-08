from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            space = Space(row["id"], row["address"], row["description"], row["price"], row["host_id"])
            spaces.append(space)
        return spaces
    
    def add(self, space):
        rows = self._connection.execute('INSERT INTO spaces (address, description, price, host_id) VALUES (%s, %s, %s, %s) RETURNING id', [space.address, space. description, space.price, space.host_id])
        