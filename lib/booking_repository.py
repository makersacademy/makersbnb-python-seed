from lib.booking import Booking


class BookingRepository():
    def __init__(self, connection):
        self._connection = connection
        

    def create_booking(self, booking):
        self._connection.execute('INSERT INTO bookings (property_id, dates_booked_from, dates_booked_to, approved, booker_id) VALUES (%s, %s, %s, %s, %s)',
    [
        booking.property_id,
        booking.dates_booked_from,
        booking.dates_booked_to,
        booking.approved,
        booking.booker_id
    ]
)
    
    def show_user_bookings(self, booker_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE booker_id = %s", (booker_id,))

        user_bookings = []
        for row in rows:
            booking = Booking(row['property_id'], row['dates_booked_from'], row['dates_booked_to'], row['approved'], row['booker_id'])
            user_bookings.append(booking)
        return user_bookings
        
    def show_property_bookings(self,property_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE property_id = %s", (property_id,))
        property_bookings = []
        for row in rows:
            booking = Booking(row['property_id'], row['dates_booked_from'], row['dates_booked_to'], row['approved'], row['booker_id'])
            property_bookings.append(booking)
        return property_bookings