from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        result = []
        for row in rows:
            item = Space(row['id'], row['name'], row['description'], row['price'])
            result.append(item)
        return result
