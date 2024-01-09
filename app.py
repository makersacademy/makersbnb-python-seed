import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
<<<<<<<<< Temporary merge branch 1
from lib.sign_up import *
=========
from lib.listing import *
from lib.listing_repository import *
>>>>>>>>> Temporary merge branch 2

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
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return render_template('login.html', name=name, email=email, password=password)
# The above function gathers all of the details for sign up

@app.route('/login2', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/loggedin', methods=["POST"])
def submit_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    return render_template('test_loggedin.html', email=email, password=password)

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


# GET POST /sign_up
# Requests email and password from user and stores to database
# Try it:
#   ; open http://localhost:5000/sign_up
@app.route('/sign_up', methods=['GET', 'POST'])
def index():
    return render_template('sign_up.html')
def sign_up():
    email = request.form.get('email')
    password = request.form.get('password')
    if email == "":
        e_message = "Please fill in your email address"
        return render_template("registration_form.html", message=e_message)

    if password == "":
        p_message = "Please fill in your password"
        return render_template("registration_form.html", message=p_message)

    # Call the create method of UserRepository to add a new user
    UserRepository.create(email, password)

    return "User registered successfully!"

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

