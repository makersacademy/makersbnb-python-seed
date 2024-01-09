from lib.booking import Booking
from datetime import date

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            """
            SELECT * FROM bookings;
            """
        )
        bookings = []
        for row in rows:
            if row['confirmed'] == '1':
                confirmed = True
            elif row['confirmed'] == '0':
                confirmed = False
            else:
                confirmed = None
            bookings.append(
                Booking(row['id'], row['date'], row['space_id'], row['guest_id'], confirmed)
            )
        return bookings
    
    def find(self, id):
        row = self._connection.execute(
            """
            SELECT * FROM bookings WHERE id=%s;
            """, [id]
        )[0]
        if row['confirmed'] == '1':
            confirmed = True
        elif row['confirmed'] == '0':
            confirmed = False
        else:
            confirmed = None
        return Booking(row['id'], row['date'], row['space_id'], row['guest_id'], confirmed)
    
    def create(self, booking):
        date = booking.date
        space_id = booking.space_id
        date_rows = self._connection.execute(
            """
            SELECT * FROM dates where date=%s AND space_id=%s;
            """, [date.isoformat(), space_id]
        )
        if len(date_rows) > 0:
            self._connection.execute(
                """
                INSERT INTO
                """
            )
        # Then insert booking into the bookings table