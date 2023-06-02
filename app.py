import os
from flask import Flask, request, render_template, session, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import *
from lib.listings import *
from lib.bookings import *

from lib.listing_repository import ListingRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
def is_authenticated():
    if 'user_id' in session:
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = session['user_id']
        result = repo.find_by_username(username) is not None, username
        return result is not None, username
    else:
        return False, None

@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listings = repository.all()
    authenticated, username = is_authenticated()
    print("Authenticated:", authenticated)
    print("Username:", username)
    return render_template('index.html', listings=listings, authenticated=authenticated, username=username)

@app.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        username = request.form['username']
        password = request.form['password']
        repo = UserRepository(connection)
        if repo.check_password(username, password):
            session['user_id'] = username
            authenticated, username = is_authenticated()
            return render_template('index.html', username=username, authenticated=authenticated)
        else:
            error_message = "Unable to authenticate"
            return render_template('index.html', message=error_message)

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Clear the user session
    return redirect(url_for('get_index'))


@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/create', methods=['GET'])
def get_create_space_form():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    username = session['user_id']
    user = user_repo.find_by_username(username)
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    listing = Listing(None, name, description, price, user.id)
    repo.create(listing)
    return redirect(url_for('get_index'))

@app.route('/signup', methods=['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    actualname = request.form['actualname']
    username = request.form['username']
    password = request.form['signup-password']
    email = request.form['email']
    user = User(None, username, actualname, email, password)
    result = repo.create(user)
    if result == "email already has account":
        error = "email already has account"
        return render_template('signup.html', error=error)
    elif result == "username already taken":
        error = "username already taken"
        return render_template('signup.html', error=error)
    else:
        success = "You have successfully signed up, please log in"
        return render_template('signup.html', success=success)

@app.route('/book')
def make_booking_request(listing_id, date):
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    username = session['user_id']
    user = user_repo.find_by_username(username)
    booking = Booking(None, user, listing_id, date, False)
    #what template do we want to return?
    
# @app.route('/signup') #gets the booking requests
# def get_host_booking_requests():



@app.route('/signup')
def get_signup():
    return render_template('signup.html')


app.secret_key = 'your very secret key'


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
