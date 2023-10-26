import os
from flask import Flask, flash, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.listing_repo import *
from lib.user import *
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'thisisasupersecretkey'


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

#sign up page
@app.route('/index', methods=['POST'])
def post_index():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(None, username, email, password)
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    repo.create(user)
    return redirect(f"/spaces")

#log in page get
@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

#log in page post - log in a user with username and password
@app.route('/login', methods=['POST'])
def post_login():
    username = request.form['username']
    password = request.form['password']
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    user = repo.get_user_by_username(username)
    if user.username == username and user.password == password:
        session['logged_in'] = True
        return redirect('/spaces')
    else:
        flash('Invalid username or password', 'error')
        return redirect('/login')
    
@app.route('/logout',methods=['POST'])
def logout():
    session['logged_in'] = False
    return redirect('/login')




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

@app.route('/spaces/<id>', methods=['GET'])
def get_spaces_id(id):
    connection = get_flask_database_connection(app)
    repo = ListingRepo(connection)
    listing = repo.find_with_listing_id(id)
    return render_template('booking.html', listing=listing)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
