import psycopg
from lib.booking import Booking

class BookingRepository():
    def __init__(self, connection):
        self._connection = psycopg.connect(connection)

    def find(self, user_id):
        result = self._connection.execute("SELECT * FROM bookings WHERE user_id = %s", user_id)
        if result:
            bookings = []
            for row in result:
                bookings.append(Booking(row.id, row.user_id, row.date_booked))
            return bookings
        else:
            return None
    
    def create(self, booking):
        self._connection.execute("INSERT INTO bookings (user_id, date_booked) VALUES (%s, %s) RETURNING user_id, date_booked", booking.user_id, booking.date_booked)
        return None