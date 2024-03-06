from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_start_date'], row['booking_end_date'], row['space_id'])
            bookings.append(item)
        return bookings
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [id])
        row = rows[0]
        return Booking(row['id'], row['booking_start_date'], row['booking_end_date'], row['space_id'])
    
    def create(self, booking_start_date, booking_end_date, space_id):
        self._connection.execute('INSERT INTO bookings (booking_start_date, booking_end_date, space_id) VALUES (%s, %s, %s)', [booking_start_date, booking_end_date, space_id])

    def update(self, booking):
        self._connection.execute('UPDATE bookings SET booking_start_date = %s, booking_end_date = %s, space_id = %s WHERE id = %s', [booking.booking_start_date, booking.booking_end_date, booking.space_id, booking.id])
        
    def delete(self, id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [id])