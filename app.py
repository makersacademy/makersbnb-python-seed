import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.list_a_space import Listing
from lib.list_a_spaceRepository import ListingRepository

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

@app.route('/signup')
def get_signup():
    return render_template('sign_up.html')

@app.route('/signup', methods=['POST'])
def add_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    user_created = False

    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    user = User(None, name, username, email, password)
    repository.add(user)

    user_created = True

    return render_template('sign_up.html', user_created=user_created)

@app.route('/new_listing', methods=['GET'])
def get_new_listing():
    return render_template('new_listing.html')

@app.route('/new_listing', methods = ['POST'])
def add_new_listing():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)

    listing_created = False

    name = request.form['Name']
    description = request.form['Description']
    price = request.form['Price_per_night']

    listing = Listing(name, description, price)
    repository.add(listing)

    listing_created = True

    if listing_created == True:
        return render_template('new_listing.html', listing_created=listing_created)
    else:
        return render_template('new_listing.html')
    
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
