from lib.bookings import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        
        bookings = []
        print("rows:", rows)
        for row in rows:
            item = Booking(row['id'], row['requester_id'], row['listing_id'], row['booking_date'], row['approved'] )
            bookings.append(item)
        print(bookings)
        return bookings
    
    def create(self, booking):
        self._connection.execute(
        'INSERT INTO bookings (requester_id, listing_id, booking_date, approved) VALUES (%s, %s, %s, %s)', 
        [booking.requester_id, booking.listing_id, booking.booking_date, booking.approved]
    )
        
    
    # def get_all_pending_booking_requests(self, host_id):
    #     query = '''
    #     SELECT bookings.*
    #     FROM bookings
    #     JOIN listings ON listings.id = bookings.listing_id
    #     WHERE listings.user_id = %s
    #     AND bookings.approved = FALSE
    # '''
    #     rows = self._connection.execute(query, [host_id])
    #     print(rows)
    #     bookings = []
    #     print("bookings:", bookings)
    #     for row in rows:
    #         item = Booking(row['id'], row['requester_id'], row['listing_id'], row['booking_date'], row['approved'] )
    #     bookings.append(item)
    #     return bookings
        
        

    # def get_all_approved_booking_requests(self, host_id):
    #     query = '''
    #     SELECT bookings.*
    #     FROM bookings
    #     JOIN listings ON listings.id = bookings.listing_id
    #     WHERE listings.user_id = %s
    #     AND bookings.approved = TRUE
    #     '''
    #     rows = self._connection.execute(query, [host_id])
    #     bookings = []
    #     for row in rows:
    #         item = Booking(row['id'], row['requester_id'], row['listing_id'], row['booking_date'], row['approved'] )
    #     bookings.append(item)
    #     return bookings
        