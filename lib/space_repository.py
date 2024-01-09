from lib.space import Space

class SpaceRepository():
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM spaces')
        spaces = []

        for row in rows:
            space = Space(row['id'], row['name'], row['description'], row['price'], row['start_date'], row['end_date'])
            spaces.append(space)
        return spaces


    def find(self, space_id):
        rows = self.connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row['id'], row['name'], row['description'], row['price'], row['start_date'], row['end_date'])
    

    def create(self, space):
        self.connection.execute('INSERT INTO spaces(name, description, price, start_date, end_date) VALUES (%s, %s, %s, %s, %s)', [space.name, space.description, space.price, space.start_date, space.end_date])
        return None
    