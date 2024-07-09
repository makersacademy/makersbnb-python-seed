from lib.BookingRequest import BookingRequest

from datetime import datetime

class BookingRequestRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        # TODO - Remove hardcoded sql.
        rows = self._connection.execute('SELECT property_id, user_id, start_date, end_date from bookings') 
        booking_requests = []
        for row in rows:

            end_date_obj = row["end_date"]
            start_date_obj = row["start_date"]

            br =  BookingRequest(start_date_obj, end_date_obj, row["property_id"], row["user_id"])
            print(row) # TODO - Remove
            
            booking_requests.append(br)

        return booking_requests
    
    # def create(self, BookingRequest):
    #     # Need SQL from Charlie and Tara.
    #     rows = self._connection.execute(
    #         'INSERT INTO booking_request (start_date, end_date, property_id, customer_id) VALUES (%s, %s, %s, %s) Returning Id', 
    #         [BookingRequest.start_date, BookingRequest.end_date, BookingRequest.property_id, BookingRequest.customer_id])
    #     # BookingRequest.id = rows[0]['id'] - Not sure if we need this yet.
    #     return None
    
    # # Delete a BookingReference.
    # def delete(self, booking_request_id):
    #     # Need SQL from Charlie and Tara.
    #     self._connection.execute(
    #         'DELETE FROM REQUESTS WHERE id = %s', [booking_request_id])
    #     return None
    
    # # Find bookingReferences by their requester.
    # def find_by_customer(self, customer_id):
        
    #     booking_requests= []
    #     # Need SQL from Charlie and Tara.
    #     rows = self._connection.execute(
    #         'SELECT * from REQUESTS WHERE customer_id = %s', [customer_id])
    #     for row in rows:
    #         br =  BookingRequest(row["start_date"], row["end_date"], row["property_id"], row["customer_id"])
    #         booking_requests.append(br)
    #     return booking_requests
    
    # # Find bookingReferences by their property.
    # def find_by_property(self, property_id):
        
    #     booking_requests= []
    #     # Need SQL from Charlie and Tara.
    #     rows = self._connection.execute(
    #         'SELECT * from REQUESTS WHERE property_id = %s', [property_id])
    #     for row in rows:
    #         br =  BookingRequest(row["start_date"], row["end_date"], row["property_id"], row["customer_id"])
    #         booking_requests.append(br)
    #     return booking_requests