import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from datetime import datetime
from lib.space_repository import *
from lib.booking import *
from lib.booking_repository import *


# Create a new Flask app
app = Flask(__name__)
app.date = None

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    # to check if login information is valid we'll need user.py
    return render_template('login.html')


@app.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html')



@app.route('/1/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/1/spaces', methods=['POST'])
def get_spaces_available_spaces():
    connection = get_flask_database_connection(app)
    date = request.form['Pick A Date']
    datetimevar = datetime.strptime(str((date)), '%Y-%m-%d').date()
    spacerepo = SpaceRepository(connection)
    spaces = []
    available_list = spacerepo.in_window(datetimevar)
    for space in available_list:
        if spacerepo.is_available(space.id, datetimevar):
            spaces.append(space)
    return render_template('spaces_available.html', spaces = spaces, date = date)

@app.route('/1/book/<int:id>/', methods = ['POST'])
def book_date(id):
    connection = get_flask_database_connection(app)
    date = request.form['date']
    spacerepo = SpaceRepository(connection)
    space = spacerepo.find_by_id(id)
    return render_template('book.html', date = date, space = space)

@app.route('/1/current_book/<int:id>/', methods = ['POST'])
def make_booking(id):
    connection = get_flask_database_connection(app)
    date = request.form['date']
    current_booking = Booking(None, date, 1, id)
    bookrepo = BookingRepository(connection)
    bookrepo.create(current_booking)
    return redirect('/1/spaces')



@app.route('/1/spaces/new', methods=['GET'])
def create_a_space():
    return render_template('create_space.html')


@app.route('/1/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')


@app.route('/1/requests', methods=['POST'])
def post_requests():
    return render_template('requests.html')


@app.route('/1/spaces/1', methods=(['GET']))  # change 1 to id later
def post_request_space():
    return render_template('single_space.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
