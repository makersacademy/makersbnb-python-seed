import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection

from lib.sign_up import *

from lib.listing import *
from lib.listing_repository import *


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


# @app.route('/test', methods=['GET'])
# def get_test():
#     return render_template('test.html')

@app.route('/login', methods=["POST"])
def submit_signup():
    connection = get_flask_database_connection(app)
    userRepo = UserRepository(connection)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if email == "":
        message="Please fill in your email"
        return render_template('login.html', message=message)
    if password == "":
        message="Please fill in your password"
        return render_template('login.html', message=message)
    userRepo.create(email, password)
    return render_template('login.html', name=name, email=email, password=password)
# The above function gathers all of the details for sign up

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/loggedin', methods=["POST"])
def submit_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    userRepo = UserRepository(connection)
    checker = userRepo.check_password(email, password)
    if checker:
        return render_template('test_loggedin.html', email=email, password=password)
    else:
        message = "Incorrect details" 
        return render_template('login.html', message = message)

@app.route('/adminlogin', methods=['GET'])
def loggedin_page():
    return render_template('test_loggedin.html')
#----------------------------------------------#
#Bookings

@app.route('/book', methods=['GET'])
def booking_page():
    #testing authentication
    email = request.args['email']
    return render_template('booking.html', email=email)

@app.route('/requests', methods=['GET'])
def request_page():
    #testing authentication
    email = request.args['email']
    return render_template('requests.html', email=email)

@app.route('/create', methods=['GET'])
def get_data():
    return render_template('create.html')

@app.route('/create', methods=['POST'])
def post_data():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    listing = Listing(None, title, description, price)
    listing = repo.insert(listing)
    return redirect(f'/listings/{listing.id}')

@app.route('/listings/<int:id>', methods=['GET'])
def get_listing(id):
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    listing = repo.select(id)
    return render_template('listing.html', listing = listing)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

