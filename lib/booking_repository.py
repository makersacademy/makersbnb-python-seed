from lib.booking import Booking

class BookingRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all bookings
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["date"], row["status"], row["space_id"], row["guest_id"])
            bookings.append(item)
        return bookings

    # Find a single booking by its id
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [booking_id])
        row = rows[0]
        return Booking(row["id"], row["date"], row["status"], row["space_id"], row["guest_id"])

    # Create a new booking
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (date, status, space_id, guest_id) VALUES (%s, %s, %s, %s) RETURNING id', [
            booking.date, booking.status, booking.space_id, booking.guest_id])
        booking.id = rows[0]["id"]
        return booking

    # Delete a booking by its id
    def delete(self, booking_id):
        self._connection.execute(
            'DELETE FROM bookings WHERE id = %s', [booking_id])
        return None