from lib.booking import Booking
from datetime import timedelta, datetime, date

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        return [Booking(row['id'], row['night_id'], row['user_id'], row['status']) for row in rows]
    
    def find(self, booking_id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s',[booking_id])
        row = rows[0]
        return Booking(row['id'], row['night_id'], row['user_id'], row['status'])
    
    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (night_id, user_id, status) VALUES (%s, %s, %s)',[
            booking.night_id, booking.user_id, booking.status
        ])
        return None
    
    def find_all_bookings_and_spaces_by_user_id(self, user_id):
        rows = self._connection.execute('''
                                        SELECT bookings.id, bookings.night_id, bookings.user_id, bookings.status,
                                        availability.id, availability.space_id, availability.date,
                                        spaces.name, spaces.price_per_night
                                        FROM bookings
                                        JOIN availability ON bookings.night_id = availability.id
                                        JOIN spaces on availability.space_id = spaces.id
                                        WHERE bookings.user_id = %s
                                        ORDER BY bookings.id
                                        ''',
                                        [user_id])
        
        #requests will contain all of the requests
        requests = []
        #Current request is used in handling consecutive dates and to put them as part of the same request
        current_request = None

        for row in rows:

            if (current_request and 
                current_request['space_id'] == row['space_id'] and 
                current_request['date_to'] + timedelta(days=1) == row['date']):
                current_request['date_to'] = row['date']
            else:
                if current_request:
                    requests.append(current_request)

                current_request = {
                    'name': row['name'],
                    'space_id': row['space_id'],
                    'date_from': row['date'],
                    'date_to': row['date'],
                    'price_per_night': row['price_per_night'],
                    'status': row['status']
                }
        
        #catches last request and adds it to the requests list
        if current_request:
            requests.append(current_request)
        
        return requests
