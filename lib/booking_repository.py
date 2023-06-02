class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    # def all(self):
    #     rows = self._connection.execute('SELECT * from bookings')
    #     listings = []
    #     for row in rows:
    #         item = Listing(row["id"], row["name"], row["description"], row["price"], row['user_id'])
    #         listings.append(item)
    #     return listings
    
    def create(self, booking):
        self._connection.execute(
        'INSERT INTO bookings (reqester_id, listing_id, booking_date, approved) VALUES (%s, %s, %s, %s)', 
        [booking.requester_id, booking.listing_id, booking.booking_date, booking.approved]
    )
    
    def get_all_pending_booking_requests(self, host_id):
        query = '''
        SELECT bookings.*
        FROM bookings
        JOIN listings ON listings.id = bookings.listing_id
        WHERE listings.user_id = %s
        AND bookings.approved IS NULL
    '''
        return self._connection.execute(query, [host_id])

    def get_all_approved_booking_requests(self, host_id):
        query = '''
        SELECT bookings.*
        FROM bookings
        JOIN listings ON listings.id = bookings.listing_id
        WHERE listings.user_id = %s
        AND bookings.approved = TRUE
        '''
        return self._connection.execute(query, [host_id])