import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.BookingRequestRepository import BookingRequestRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'bedsforbodies_crew'
# == Your Routes Here ==

# http://127.0.0.1:5001/index
# http://127.0.0.1:5001/spaces
# http://127.0.0.1:5001/spaces/new
# http://127.0.0.1:5001/requests


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
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
    print(bookings_list) # TODO remove
    return render_template('requests.html', bookings_list = bookings_list)

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


