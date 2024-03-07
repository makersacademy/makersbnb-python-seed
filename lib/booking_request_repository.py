from lib.booking_request import BookingRequest

class BookingRequestRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all requests
    def all(self):
        rows = self._connection.execute('SELECT * from booking_request')
        booking_requests = []
        for row in rows:
            item = BookingRequest(row["id"], row["booking_id"], row["request_status"])
            booking_requests.append(item)
        return booking_requests

    # Find a single request by it's id
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * from booking_requests WHERE id = %s', [booking_id])
        row = rows[0]
        return BookingRequest(row["id"], row["booking_id"], row["request_status"])

    # Create a new booking
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, booking_request):
        self._connection.execute('INSERT INTO booking_requests (booking_id, request_status) VALUES (%s, %s)', [
                                 booking_request.booking_id, booking_request.request_status])
        return None

    # Delete booking by it's id
    def delete(self, booking_id):
        self._connection.execute(
            'DELETE FROM booking_requests WHERE id = %s', [booking_id])
        return None 