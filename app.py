import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.booking_repository import BookingRepository
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/spaces/<int:id>', methods=['GET'])
def get_space_page(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template("space.html", space=space)


@app.route('/profile/<int:id>', methods=['GET'])
def get_profile_page(id):
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        space_repository = SpaceRepository(connection)
        user_repository = UserRepository(connection)
        username = user_repository.get_username_by_id(id)
        bookings = booking_repository.find_user_bookings(id)
        spaces = space_repository.find_user_spaces(id)

        return render_template('profile.html', username=username, spaces=spaces, bookings=bookings)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
