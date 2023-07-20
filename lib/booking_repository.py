from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            bookings.append(Booking(row["id"], row["start_date"], row["end_date"], row["property_id"], row["user_id"]))
        print(type(bookings[1].start_date))
        return  bookings

    def find(self, id):
        row = self.connection.execute('SELECT * FROM bookings WHERE id=%s', [id])
        row = row[0]
        return Booking(row["id"], row["start_date"], row["end_date"], row["property_id"], row["user_id"])


    def create(self,booking):
        row = self.connection.execute('INSERT INTO bookings(start_date, end_date, property_id, user_id) VALUES (%s,%s,%s,%s) RETURNING id',[
            booking.start_date, booking.end_date, booking.property_id, booking.user_id])
        booking.id = row[0]["id"]
        return booking
    
    