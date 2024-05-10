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
    def get_bookings_by_user(self,user_id):
        rows = self.connection.execute(
            'SELECT * FROM bookings WHERE user_id = %s',(user_id,)
        )
        
        bookings = []
        for row in rows:
            booking = Booking(
                row['id'],
                row['date_id'],
                row['user_id'],
            )
            bookings.append(booking)
        return bookings
    
    def get_bookings_by_space(self, space_id):
        query = """
            SELECT b.id, b.date_id, b.user_id, d.confirmed, s.name
            FROM bookings b
            JOIN dates d ON b.date_id = d.id
            JOIN spaces s ON d.space_id = s.id
            WHERE d.space_id = %s
        """
        rows = self.connection.execute(query, (space_id,))
        bookings = []
        for row in rows:
            booking = Booking(
                row["id"],
                row["date_id"],
                row["user_id"]
        )
        space_name = row["name"]
        confirmed = row["confirmed"]
        bookings.append((booking, space_name, confirmed))
        return bookings if bookings else [("No bookings made for this space",)]



    
    def get_bookings_with_space_names(self, user_id):
        query = """
            SELECT b.id, b.date_id, b.user_id, s.name, d.confirmed 
            FROM bookings b
            JOIN dates d ON b.date_id = d.id
            JOIN spaces s ON d.space_id = s.id
            WHERE b.user_id = %s
        """
        rows = self.connection.execute(query, (user_id,))
        bookings = []
        for row in rows:
            booking = Booking(
                row["id"],
                row["date_id"],
                row["user_id"]
            )
        space_name = row["name"]
        confirmed = row["confirmed"]
        bookings.append((booking, space_name, confirmed))
        return bookings
    
    