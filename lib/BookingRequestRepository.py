from lib.BookingRequest import BookingRequest

from datetime import datetime

class BookingRequestRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):

        rows = self._connection.execute('SELECT property_id, user_id, start_date, end_date, id from bookings') 
        booking_requests = []
        for row in rows:

            end_date_obj = row["end_date"]
            start_date_obj = row["start_date"]

            br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"], row["id"])
            
            booking_requests.append(br)

        return booking_requests
    
    def create(self, BookingRequest):
       
        rows = self._connection.execute(
            'INSERT INTO bookings (property_id, user_id, start_date, end_date) VALUES (%s, %s, %s, %s)', 
            [BookingRequest.property_id, BookingRequest.user_id, BookingRequest.start_date, BookingRequest.end_date])
        return None
    
    # Delete a BookingReference.
    def delete(self, booking_request_id):
        self._connection.execute(
            'DELETE FROM bookings WHERE id = %s', [booking_request_id])
        return None

    
    # Find bookingReferences by their requester.

    def get_bookings_by_customer(self, user_id):
        
        booking_requests= []

        rows = self._connection.execute('SELECT * from bookings WHERE user_id = %s', [user_id])
        
        for row in rows:

            end_date_obj = row["end_date"]
            start_date_obj = row["start_date"]

            br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"], row["id"])            
            booking_requests.append(br)

            return booking_requests
    
    # Find bookingReferences by their property.
    def get_bookings_by_property(self, property_id):
        
        booking_requests= []

        rows = self._connection.execute(
            'SELECT * from bookings WHERE property_id = %s', [property_id])

        
        for row in rows:

            end_date_obj = row["end_date"]
            start_date_obj = row["start_date"]

            br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"], row["id"])            

            booking_requests.append(br)

        return booking_requests