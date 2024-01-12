from lib.booking import Booking

class BookingRepository():
    def __init__(self, connection):
        self._connection = connection


# get all, create, delete, confirm (True/False)
        
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], str(row["date"]), row["confirmed"], row['rejected'], row["user_id"], row["space_id"])
            bookings.append(item)
        return bookings
    
    def find_all_by_user(self, user_id):
        rows = self._connection.execute('SELECT * from bookings WHERE user_id = %s', [user_id])
        bookings = []
        for row in rows:
            item = Booking(row["id"], str(row["date"]), row["confirmed"], row['rejected'], row["user_id"], row["space_id"])
            bookings.append(item)
        return bookings
    
    def find_all_by_space(self, space_id):
        rows = self._connection.execute('SELECT * from bookings WHERE space_id = %s', [space_id])
        bookings = []
        for row in rows:
            item = Booking(row["id"], str(row["date"]), row["confirmed"], row['rejected'], row["user_id"], row["space_id"])
            bookings.append(item)
        return bookings

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [id])
        row = rows[0]
        return Booking(row["id"], str(row["date"]), row["confirmed"], row['rejected'], row["user_id"], row["space_id"])

    def create(self, booking):
        rows = self._connection.execute('INSERT INTO bookings (date, confirmed, rejected, user_id, space_id) VALUES (%s, %s, %s, %s, %s) RETURNING ID', [booking.date, booking.confirmed, booking.rejected, booking.user_id, booking.space_id])
        return rows[0]['id']
    
    def delete(self, id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [id])
        return None
    
    def confirm(self, id):
        self._connection.execute('UPDATE bookings SET confirmed=TRUE WHERE id = %s', [id])
        return None
    
    def reject(self, id):
        self._connection.execute('UPDATE bookings SET rejected=TRUE WHERE id = %s', [id])
    
    def already_booked(self, booking):
        bookings = self.find_all_by_space(booking.space_id)
        for item in bookings:
            print(item.date, booking.date)
            print(type(item.date), type(booking.date))
            if item.date == booking.date and item.confirmed:
                return True
        return False