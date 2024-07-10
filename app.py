import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

from lib.BookingRequestRepository import BookingRequestRepository

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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
