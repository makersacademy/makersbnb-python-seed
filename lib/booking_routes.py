from flask import render_template
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository
from lib.database_connection import get_flask_database_connection

def apply_booking_routes(app):
    
    @app.route('/bookings', methods=['GET'])
    def get_booking():
        user_id = 1  # Replace with user session id
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        space_repository = SpaceRepository(connection)
        
        # Fetch booking requests made by the user
        user_bookings = booking_repository.get_bookings_with_space_names(user_id)
        user_booking_requests = [(booking, space_name, confirmed) for booking, space_name, confirmed in user_bookings]
        
        # Fetch booking requests received by the user
        user_space_listings = space_repository.get_spaces_by_user(user_id)
        requests_received = []
        for space in user_space_listings:
            space_bookings = booking_repository.get_bookings_by_space(space.id)
            for booking in space_bookings:
                booking_obj, space_name, confirmed = booking
                requests_received.append((booking_obj, space_name, confirmed))
                
        return render_template('bookings.html', user_booking_requests=user_booking_requests, requests_received=requests_received)
