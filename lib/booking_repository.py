from lib.booking import Booking

class BookingRepository():
    def __init__(self, connection):
        self._connection = connection


# get all, create, delete, confirm (True/False)
        
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], str(row["date"]), row["confirmed"], row["user_id"], row["space_id"])
            bookings.append(item)
        return bookings

    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (date, confirmed, user_id, space_id) VALUES (%s, %s, %s, %s)', [booking.date, booking.confirmed, booking.user_id, booking.space_id])
        return None