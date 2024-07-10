import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.PropertyRepository import PropertyRepository
from lib.BookingRequestRepository import BookingRequestRepository
from lib.Property import Property

# Create a new Flask app
app = Flask(__name__)

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
        infotoprint += [(user, space["description"], space["property"], space["location"], space["cost"])]
    return render_template('spaces.html', test_list = infotoprint)

# List a new space as a Property owner.
@app.route('/spaces/new', methods=['GET'])
def list_new_property():
    return render_template('spaces_new.html')

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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
