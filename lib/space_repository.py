from lib.space import *
from lib.date import *

class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price"], row["user_id"])
            spaces.append(item)
        return spaces
    
    def find(self, space_id):
        row = self._connection.execute('SELECT * from spaces WHERE id = %s', (space_id,))
        return Space(row[0]["id"], row[0]["name"], row[0]["description"], row[0]["price"], row[0]["user_id"])
    
    def create(self, name, description, price, user_id):
        rows = self._connection.execute('INSERT INTO spaces (name, description, price, user_id) VALUES (%s, %s, %s, %s) RETURNING id', (name, description, price, user_id))
        return rows[0]["id"]
    
    def delete(self, space_id):
        self._connection.execute('DELETE from spaces WHERE id = %s', (space_id,))
        return None
    
    def find_space_and_dates(self, space_id):
        rows = self._connection.execute('SELECT * from spaces JOIN dates ON spaces.id = dates.space_id WHERE spaces.id = %s', (space_id,))
        dates = []
        for row in rows:
            date = Date(row["id"], str(row["date"]), row["confirmed"], row["space_id"])
            dates.append(date)
        space = Space(rows[0]['space_id'], rows[0]['name'], rows[0]['description'], rows[0]['price'], rows[0]['user_id'], dates)
        return space
    
    def get_spaces_by_user(self, user_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE user_id = %s', (user_id,))
        spaces = []
        for row in rows:
            space = Space(row["id"], row["name"], row["description"], row["price"], row["user_id"])
            spaces.append(space)
        return spaces