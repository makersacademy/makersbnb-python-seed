from lib.space import Space
from lib.booking import *
class SpaceRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        all_spaces = []
        for row in rows:
            item = Space(row["id"], row["title"], str(row["start_date"]), str(row["end_date"]), row['userid'], row['price'])
            all_spaces.append(item)
        return all_spaces
    
    def find_by_id(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id])
        if rows:
            row = rows[0]
            return Space(row["id"], row["title"], str(row["start_date"]), str(row["end_date"]),row['userid'],row['price'])
        else:
            raise Exception('Space not found!')
    
    def create(self, space):
        rows = self._connection.execute('INSERT INTO spaces (title, start_date, end_date, userid, price) VALUES (%s, %s, %s, %s,%s) RETURNING id', [
                                space.title, space.start_date, space.end_date, space.userid, space.price])
        row = rows[0]
        space.id = row["id"]
        return space
    
    def is_available(self, space_id, date):
        rows = self._connection.execute('SELECT * from bookings WHERE space_id = %s AND booking_date = %s', [space_id, str(date)])
        if rows:
            return False
        else:
            return True
        # pre_booked = []
        # for row in rows:
        #     item = Booking(row['id'],row['booking_date'], row['space_id'],row['user_id'])
        #     pre_booked.append(item)
        return pre_booked
    
