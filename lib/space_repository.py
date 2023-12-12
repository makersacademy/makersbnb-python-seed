from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM spaces')
        spaces = []

        for row in rows:
            space = Space(row['id'], row['name'], row['description'], row['price'])
            spaces.append(space)
        return spaces


