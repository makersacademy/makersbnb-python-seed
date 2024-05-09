from flask import render_template
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository
from lib.database_connection import get_flask_database_connection

def apply_booking_routes(app):
    
    @app.route('/bookings', methods =['GET'])
    def get_booking():
        user_id = 1  # Replace with user session id
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        space_repository = SpaceRepository(connection)

        # Get booking requests made by the user
        user_booking_requests = booking_repository.get_bookings_with_space_names(user_id)

        # Get booking requests received by the user
        user_space_listings = space_repository.get_spaces_by_user(user_id)
        requests_received = []
        for space in user_space_listings:
            requests_received.extend(booking_repository.get_bookings_by_space(space.id))

        return render_template('bookings.html', user_booking_requests=user_booking_requests, requests_received=requests_received)
