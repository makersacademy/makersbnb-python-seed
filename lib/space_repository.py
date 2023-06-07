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