from lib.booking import *

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection 
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM bookings")
        bookings = []
        for row in rows:
            booking = Booking(row["user_id"], row["space_id"], row["booking_date"], row["booking_status"])
            bookings.append(booking)
        return bookings


    def find(self, user_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        row = rows [0]
        booking = Booking(row["user_id"], row["space_id"], row["booking_date"], row["booking_status"])
        return booking
    
    
    def create(self, new_booking):
        self._connection.execute("INSERT INTO bookings (user_id, space_id, booking_date, booking_status) VALUES (%s, %s, %s, %s)",
                            [new_booking.user_id, new_booking.space_id, new_booking.booking_date, new_booking.booking_status])