from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        return [Booking(row['id'], row['night_id'], row['user_id'], row['status']) for row in rows]
    
    def find(self, booking_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s',[booking_id])
        row = rows[0]
        return Booking(row['id'], row['night_id'], row['user_id'], row['status'])
    
    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (night_id, user_id, status) VALUES (%s, %s, %s)',[
            booking.night_id, booking.user_id, booking.status
        ])
        return None

    def update_status(self, button_press, booking_id):
        self._connection.execute('UPDATE bookings SET status = %s WHERE id = %s', [button_press, booking_id])
        return None