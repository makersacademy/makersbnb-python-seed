import os
from flask import Flask, request, render_template, redirect, flash, url_for
from lib.database_connection import get_flask_database_connection
from lib.user import *
from lib.user_repository import *
from lib.space_repository import SpaceRepository
from lib.booking_repository import *

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('homepage.html')

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    users = repository.all()
    users_string = ''
    for user in users:
        users_string += f'{user.email} - {user.password}\n'
    return users_string

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def user_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    email = request.form['email']
    password = request.form['password']

    return redirect(url_for(signup_page))

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def add_new_user():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

        # Get the fields from the request form
    email = request.form['email']
    password = request.form['password']

        # Create a book object
    user = User(None, email, password)

        # Check for validity and if not valid, show the form again with errors
    if not user.is_valid():
        return 400

        # Save the book to the database
    user = repository.create(user)

        # Redirect to the book's show route to the user can see it
    return redirect("/users")

# login

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces)

@app.route('/spaces/<int:id>', methods=['GET'])
def get_single_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('space_page.html', space=space)

@app.route('/book_space', methods=['POST'])
def book_space():
    space_id = request.form['space_id']
    user_id = request.form['user_id'] # <-- session thing here OR in space_page.html
    date = request.form['date']
    price = request.form['price']

    booking_repo = BookingRepository(get_flask_database_connection(app))
    success = booking_repo.create_booking(space_id, user_id, date, price)

    if success:
        # flash('Venue booked successfully!', 'success')
        return redirect(url_for('user_page'))
    else:
        # flash('Venue is unavailable for the selected date.', 'error')
        return 'Venue is unavailable for the selected date. Please go back and choose another date.'

    return redirect(url_for('get_spaces'))

@app.route('/my_account', methods=['GET'])
def user_page():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    my_bookings = booking_repo.find(1) # <-- session thing here
    space_repo = SpaceRepository(connection)
    spaces = space_repo.all()
    return render_template('user_page.html', my_bookings = my_bookings, spaces = spaces)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

