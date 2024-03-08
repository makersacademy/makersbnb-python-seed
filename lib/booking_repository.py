from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'], row['space_id'])
            bookings.append(item)
        return bookings
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [id])
        row = rows[0]
        return Booking(row['id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'], row['space_id'])
    
    def create(self, booking_from, booking_to, bookers_id, space_id):
        self._connection.execute('INSERT INTO bookings (booking_from, booking_to, bookers_id, space_id) VALUES (%s, %s, %s, %s)', [booking_from, booking_to, bookers_id, space_id])

    def update(self, booking):
        self._connection.execute('UPDATE bookings SET booking_from = %s, booking_to = %s, space_id = %s WHERE id = %s', [booking.booking_from, booking.booking_to, booking.space_id, booking.id])
        
    def delete(self, id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [id])

    def find_space(self, space_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE space_id = %s', [space_id])
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'], row['space_id'])
            bookings.append(item)
        return bookings

    def find_requests_outstanding(self, space_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE request_outstanding = True and space_id = %s', [space_id])
        requests = []
        for row in rows:
            item = Booking(row['id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'], row['space_id'])
            requests.append(item)
        return requests

    def find_bookings(self, bookers_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE bookers_id = %s', [bookers_id])
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'], row['space_id'])
            bookings.append(item)
        return bookings

    def get_booking_from(self, space_id):
        query = "SELECT booking_from FROM bookings WHERE space_id = %s"
        rows = self._connection.execute(query, [space_id])
        booking_from = []
        for row in rows:
            item = row['booking_from']
            booking_from.append(item)
        return booking_from

    def get_booking_to(self, space_id):
        query = "SELECT booking_to FROM bookings WHERE space_id = %s"
        rows = self._connection.execute(query, [space_id])
        booking_to = []
        for row in rows:
            item = row['booking_to']
            booking_to.append(item)
        return booking_to

    def accept_booking(self, bookers_id):
        self._connection.execute('UPDATE bookings SET booked = True WHERE id = %s', [bookers_id])