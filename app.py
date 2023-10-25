import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.listing_repo import *
from lib.user import *
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def post_index():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(None, username, email, password)
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    repo.create(user)
    return '', 200

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo = ListingRepo(connection)
    listings = repo.all()
    print(listings)
    return render_template('spaces.html', listings=listings)

@app.route('/spaces/new', methods=['GET'])
def get_new():
    return render_template('new.html')

@app.route('/spaces', methods=['POST'])
def post_spaces():
    listing_name = request.form['name']
    listing_description = request.form['description']
    listing_price = request.form['price']
    user_id = request.form['user_id']
    connection = get_flask_database_connection(app)
    repo = ListingRepo(connection)
    repo.add(listing_name, listing_description, float(listing_price), int(user_id))
    return redirect(f"/spaces")
    


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
