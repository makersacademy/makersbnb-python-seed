from lib.booking import *
class BookingRepository:
    def __init__(self, connection):
        self.connection = connection

    def find_by_spaceid(self, spaceid):
        booking_list = []
        rows = self.connection.execute('SELECT * FROM bookings WHERE space_id = %s',[spaceid])
        if rows:
            for row in rows:
                existing_booking = Booking(row['id'],row['booking_date'], row['space_id'],row['user_id'])
                booking_list.append(existing_booking)
            return booking_list
        else:
            return booking_list
        
    def create(self, booking):
        self.connection.execute('INSERT INTO users (booking_date, space_id, user_id) Values(%s, %s, %s)',[str(booking.date), booking.spaceid, booking.userid])
        
    def find_by_id(self, id):
        rows = self.connection.execute('SELECT * FROM bookings WHERE id = %s',[id])
        if rows:
            row = rows[0]
            return Booking(row['id'], row['booking_date'],row['space_id'], row['user_id'])
        else:
            raise Exception("Booking not found!")

    def all(self):
        rows = self.connection.execute('SELECT * FROM bookings')
        booking_list = []
        for row in rows:
            current_booking = Booking(row['id'], str(row['booking_date']),row['space_id'], row['user_id'])
            booking_list.append(current_booking)
        return booking_list


