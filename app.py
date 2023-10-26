import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.database_connection import DatabaseConnection


# Create a new Flask app
app = Flask(__name__)

connection = DatabaseConnection()
connection.connect()
# Seed with some seed data
connection.seed("seeds/makersbnb.sql")

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:

# open http://localhost:5000/index


@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/register', methods=['GET'])
def new_registration():

    return render_template('register.html')


@app.route('/register', methods=['POST'])
def post_register():

    connection = get_flask_database_connection(app)

    username = request.form("username")
    email_address = request.form("email_address")
    password = request.form("password")

    return render_template('index.html')


@app.route('/login', methods=['GET'])
def get_login():

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def post_login():

    connection = get_flask_database_connection(app)

    username = request.form("username")
    password = request.form("password")

    return render_template('index.html')


@app.route('/booking-requests', methods=['GET'])
def get_owners_booking_requests():
    return render_template('owner_booking_requests.html')


@app.route('/add-a-space', methods=['GET'])
def get_add_a_space():
    return render_template('add_a_space.html')


@app.route('/add-a-space', methods=['POST'])
def post_space_added():
    pass


@app.route('/space', methods=['GET'])
def get_individual_space():

    connection = get_flask_database_connection(app)

    return render_template('space.html')


@app.route('/make_a_booking', methods=['GET'])  # Liza
def make_a_booking_form():
    return render_template('make_a_booking.html')


# POST /make_a_booking
# Handles the submission of a booking request
@app.route('/booking_approvement', methods=['POST'])  # Liza
def booking_approvement():
    space_name = request.form['space_name']
    date = request.form['date']
    connection.create_booking_request(space_name, date)
    return render_template('booking_approvement.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
