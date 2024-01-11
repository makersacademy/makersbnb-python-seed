from lib.booking import *

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_booking(self, space_id, user_id, date, price):
        available = self._check_availability(space_id, date)
        if available:
            self._connection.execute(
                'INSERT INTO bookings (space_id, user_id, date, price) VALUES (%s, %s, %s, %s)',
                [space_id, user_id, date, price]
            )
            return True
        return False

    def _check_availability(self, space_id, date):
        result = self._connection.execute(
            'SELECT * FROM bookings WHERE space_id = %s AND date = %s',
            [space_id, date])
        # If there is no booking for that date, then venue is available, so return True
        if not result:
            return True
        return False
    
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE user_id = %s', [user_id])
        # row = rows[0]
        my_bookings = []
        for row in rows:
            my_bookings.append(Booking(row["id"], row["space_id"], row["user_id"], row["date"], row["price"]))
        return my_bookings