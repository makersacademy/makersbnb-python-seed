from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self.connection = connection
        
    def all(self):
        rows = self.connection.execute('SELECT * FROM booking')
        bookings = []
        for row in rows:
            item = Booking(
                row["id"],
                row["user_id"],
                row["date_id"],
            )
            bookings.append(item)
        return bookings
    
    def find(self, booking_id):
        rows = self.connection.execute(
            'SELECT * from spaces WHERE id = %s', 
            [booking_id]
        )
        row = rows[0]
        return Booking(
            row[0]["id"], 
            row[0]["user_id"], 
            row[0]["date_id"]
        )
        
    def create(self, booking):
        self.connection.execute(
            'INSERT INTO bookings (user_id, date_id) VALUES (%s, %s)', 
            [booking.user_id, booking.date_id])
        return None
    
    def delete(self, booking_id):
        self.connection.execute(
            'DELETE from spaces WHERE id = %s', 
            (booking_id)
        )
        return None