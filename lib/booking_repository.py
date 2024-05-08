from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self.connection = connection
        
    def all(self):
        rows = self.connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            item = Booking(
                row["id"],
                row["date_id"],
                row["user_id"],
            )
            bookings.append(item)
        return bookings
    
    def find(self, booking_id):
        row = self.connection.execute(
            'SELECT * from bookings WHERE id = %s', 
            (booking_id,)
        )
        return Booking(
            row[0]["id"], 
            row[0]["date_id"], 
            row[0]["user_id"]
        )
        
    def create(self, booking):
        self.connection.execute(
            'INSERT INTO bookings (user_id, date_id) VALUES (%s, %s)', 
            (booking.user_id, booking.date_id))
        return None
    
    def delete(self, booking_id):
        self.connection.execute(
            'DELETE from bookings WHERE id = %s', 
            (booking_id,)
        )
        return None