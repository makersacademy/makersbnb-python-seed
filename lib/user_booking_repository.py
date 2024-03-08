from lib.user_booking import UserBooking

class UserBookingRepository:
    def __init__(self, connection):
        self._connection = connection


    
    def find_user_requests(self, id):
        rows = self._connection.execute('SELECT * FROM users_bookings WHERE user_id = %s', [id])
        user_requests = []
        for row in rows:
            item = UserBooking(row['id'], row['booking_id'], row['user_id'], row['user_name'], row['space_name'], row['space_id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'])
            user_requests.append(item)
        return user_requests

    def find_user_bookings(self, id):
        rows = self._connection.execute('SELECT * FROM users_bookings WHERE bookers_id = %s', [id])
        user_bookings = []
        for row in rows:
            item = UserBooking(row['id'], row['booking_id'], row['user_id'], row['user_name'], row['space_name'], row['space_id'], row['booking_from'], row['booking_to'], row['bookers_id'], row['request_outstanding'], row['booked'])
            user_bookings.append(item)
        return user_bookings