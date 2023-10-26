from lib.booking import Booking


class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            booking = Booking(row["id"], row["space_id"], row["booker_id"], row["start_date"], row["end_date"], row["confirmed"])
            bookings.append(booking)
        return bookings
    
    def create(self, booking):
        return self._connection.execute("INSERT INTO bookings (space_id, booker_id, start_date, end_date, confirmed) VALUES (%s, %s, %s, %s, %s) RETURNING id", [booking.space_id, booking.booker_id, booking.start_date, booking.end_date, booking.confirmed])
        
    def find(self, booking_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE id = %s", [booking_id])
        bookings = []
        for row in rows:
            booking = Booking(row["id"], row["space_id"], row["booker_id"], row["start_date"], row["end_date"], row["confirmed"])
            bookings.append(booking)
        return bookings[0]

    def delete(self, booking_id):
        self._connection.execute("DELETE FROM bookings WHERE id = %s", [booking_id])
        
    def update(self, booking_id, column, value):
        self._connection.execute(f"UPDATE bookings SET {column} = %s WHERE id = %s", [value, booking_id])