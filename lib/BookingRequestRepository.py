from lib.BookingRequest import BookingRequest

class BookingRequestRepository():


    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from bookings') # Need SQL from Charlie and Tara.
        booking_requests = []
        for row in rows:
            br =  BookingRequest(row["property_id"], row["user_id"],row["start_date"], row["end_date"])
            booking_requests.append(br)
        return booking_requests
    
    def create(self, BookingRequest):
        # Need SQL from Charlie and Tara.
        rows = self._connection.execute(
            'INSERT INTO bookings (property_id, user_id, start_date, end_date) VALUES (%s, %s, %s, %s)', 
            [BookingRequest.property_id, BookingRequest.user_id, BookingRequest.start_date, BookingRequest.end_date])
        # BookingRequest.id = rows[0]['id'] - Not sure if we need this yet.
        return None
    
    # Delete a BookingReference.
    def delete(self, booking_request_id):
        # Need SQL from Charlie and Tara.
        self._connection.execute(
            'DELETE FROM bookings WHERE id = %s', [booking_request_id])
        return None
    
    # Find bookingReferences by their requester.
    def find_by_customer(self, customer_id):
        
        booking_requests= []
        # Need SQL from Charlie and Tara.
        rows = self._connection.execute(
            'SELECT * from bookings WHERE customer_id = %s', [customer_id])
        for row in rows:
            br =  BookingRequest(row["property_id"], row["user_id"], row["start_date"], row["end_date"])
            booking_requests.append(br)
        return booking_requests
    
    # Find bookingReferences by their property.
    def find_by_property(self, property_id):
        
        booking_requests= []
        # Need SQL from Charlie and Tara.
        rows = self._connection.execute(
            'SELECT * from bookings WHERE property_id = %s', [property_id])
        for row in rows:
            br =  BookingRequest(row["property_id"], row["user_id"], row["start_date"], row["end_date"])
            booking_requests.append(br)
        return booking_requests