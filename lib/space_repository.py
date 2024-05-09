from lib.space import Space
from lib.booking import *
class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        all_spaces = []
        for row in rows:
            item = Space(row["id"], row["title"],row['price'], str(row["start_date"]), str(row["end_date"]), row['ownerid'])
            all_spaces.append(item)
        return all_spaces
    
    def find_by_id(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id])
        if rows:
            row = rows[0]
            return Space(row["id"], row["title"],row['price'], str(row["start_date"]), str(row["end_date"]), row['ownerid'])
        else:
            raise Exception('Space not found!')
    
    def create(self, space):
        rows = self._connection.execute('INSERT INTO spaces (title, start_date, end_date, ownerid, price) VALUES (%s, %s, %s, %s,%s) RETURNING id', [
                                space.title, space.start_date, space.end_date, space.ownerid, space.price])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def is_available(self, space_id, date):
        rows = self._connection.execute('SELECT * from bookings WHERE spaceid = %s AND booking_date = %s', [space_id, str(date)])
        if rows:
            return False
        else:
            return True

    
