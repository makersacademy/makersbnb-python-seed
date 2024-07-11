import os

from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection

from lib.user_repository import UserRepository
from lib.PropertyRepository import PropertyRepository
from lib.BookingRequestRepository import BookingRequestRepository
from lib.Property import Property
from lib.BookingRequest import BookingRequest

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'bedsforbodies_crew'
# == Your Routes Here ==

# http://127.0.0.1:5001/index
# http://127.0.0.1:5001/spaces
# http://127.0.0.1:5001/spaces/new
# http://127.0.0.1:5001/requests - See all the requests in the system.


@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# List available spaces.
@app.route('/spaces', methods=['GET'])
def get_spaces():
    Connection = get_flask_database_connection(app)
    infotoprint = []
    allspaces = Connection.execute('SELECT * FROM properties')
    for space in allspaces:
        user = Connection.execute('SELECT name FROM users WHERE id = %s',[space["user_id"]])
        infotoprint += [(user, space["description"], space["property"], space["location"], space["cost"], space['id'])]
    return render_template('spaces.html', test_list = infotoprint)

# List a new space as a Property owner.
@app.route('/spaces/new', methods=['GET'])
def list_new_property():
    Connection = get_flask_database_connection(app)
    #What info to pas
    return render_template('spaces_new.html')

# BOOKING REQUESTS

# See requests that I've made and received so far.
@app.route('/requests', methods=['GET'])
def get_requests():
    Connection = get_flask_database_connection(app)
    repository = BookingRequestRepository(Connection)
    bookings_list = repository.all()
    return render_template('requests.html', bookings_list = bookings_list)

# POST /spaces/new
    # Creates a new book
@app.route('/spaces/new', methods=['POST'])
def create_space():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)

    # Get the fields from the request form
    property = request.form['Property Name']
    description = request.form['Description']
    price_per_night = request.form['Price per Night (£)']
    available_from = request.form['Available From (dd-mm-yy)']
    available_to = request.form['Available To (dd-mm-yy)']

    # Create a property object
    property = Property(None, property, description, price_per_night, available_from, available_to)

    # Check for validity and if not valid, show the form again with errors
    if not property.is_valid():
        return render_template('spaces/new.html', property=property, errors=property.generate_errors()), 400

    # Save the property to the database
    property = repository.create(property)

    # Redirect to the book's show route to the user can see it
    return redirect(f"/spaces/{property.id}")

# Get details for a booking and change details.
@app.route('/booking_detail/<id>', methods=['GET'])
def get_booking_detail(id):
    Connection = get_flask_database_connection(app)
    repository = BookingRequestRepository(Connection)
    booking_details = repository.get_request_detail(id)
    return render_template('booking_detail.html', booking_details = booking_details)

@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    Connection = get_flask_database_connection(app)
    repository = PropertyRepository(Connection)
    space_info = repository.find(id)
    #space_info = Connection.execute('SELECT * FROM properties WHERE id = %s',[id])[0] #Remove Hardcoded SQL when we can get details by a method on property repo
    return render_template('space_info.html',space_info = space_info)

@app.route('/spaces/<id>', methods=['POST'])
def book_space(id):
    Connection = get_flask_database_connection(app)
    booking_repo = BookingRequestRepository(Connection)
    if 'user_id' not in session:
        return redirect(url_for('get_login'))
    else:
        Brequest = BookingRequest(request.form['Start Date'],request.form['End Date'],id,None,None,'PENDING') #To Do - User_Id, Booking_Id
        booking_repo.create(Brequest)
        return redirect(url_for('get_requests'))
    


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login_page.html')

@app.route('/login', methods=['POST'])
def post_login():
    Connection = get_flask_database_connection(app)
    user_repository = UserRepository(Connection)
    email = request.form['email']
    password = request.form['password']
    if user_repository.check_password(email, password):
        session['user_id'] = email
        return render_template('login_success.html')
    else:
        return render_template('login_error.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('get_login'))
    return f"Welcome to your dashboard, {session['user_id']}!"

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


