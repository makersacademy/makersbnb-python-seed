from lib.booking import Booking
from datetime import datetime
class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        return [Booking(row["id"], row["listing_id"], row["booked_at"], row["booker_id"], row["check_in"], row["check_out"]) for row in rows]
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * from bookings WHERE id = %s', [id])
        row = rows[0]
        return Booking(row["id"], row["listing_id"], row["booked_at"], row["booker_id"], row["check_in"], row["check_out"])
    
    def create(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (listing_id, booker_id, check_in, check_out) VALUES (%s, %s, %s, %s) RETURNING id, booked_at', [booking.listing_id, booking.booker_id, booking.check_in, booking.check_out])
        row = rows[0]
        booking.id = row["id"]
        booking.booked_at = row["booked_at"]
        return booking
    
    def delete(self, id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [id])
        return None