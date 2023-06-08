from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            items = Space(row["id"], row["title"], row["description"], row["price"], row["date_range"], row["user_id"])
            spaces.append(items)
        return spaces
    
    def create(self, space):
        new_space = self._connection.execute('INSERT into spaces (title, description, price, date_range, user_id) values (%s, %s, %s, %s, %s)', [space.title, space.description, space.price, space.date_range, space.user_id])
        return new_space
    
    def find(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["title"], row["description"], row["price"], row["date_range"], row["user_id"])
    
    def remove_date(self, space_id, date):
        date_range = self.find(space_id).date_range
        date_range.remove(date)
        self._connection.execute('UPDATE spaces SET date_range = %s WHERE id = %s', [date_range, space_id])