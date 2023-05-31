
#REMINDER: Replace flash with user friendly alternative 

import os
from flask import Flask, request, render_template, session, url_for, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.listing_repository import ListingRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'not so secret key'

# == Define Functions ==

# Password is valid function
def password_is_valid(password):
    nums = "1234567890"
    special_char = "!@#$%^&*()-_=+[]{};:,<.>/?`~"
    return len(password) >= 8 and any(char in nums for char in password) and \
            any(char in special_char for char in password)

# Username is valid function
def username_is_valid(username):
    return 0 < len(username) <= 20 and username.isalpha()

### Working on rate limit function, will implement if completed


# == Routes ==

@app.route('/', methods=['GET'])
def index():
    connection = get_flask_database_connection(app)
    listing_repository = ListingRepository(connection)
    listings = listing_repository.all()
    return render_template('listings/index.html', listings = listings)

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    if request.method == 'POST':

        user_created = False

        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Error message if email address or username is in database
        if not repository.email_is_unique(email) or not repository.username_is_unique(username):
            error_message = "Email address or username is already registered"
            return render_template('sign_up.html', error_message=error_message)
        
        # Error message if password is not valid
        if not password_is_valid(password):
            error_message = "Password must be at least 8 characters long and contain a number and special character"
            return render_template('sign_up.html', error_message=error_message)
        
        # Error message if password and confirm password do not match
        if not password == confirm_password:
            error_message = "Passwords do `ip install --upgrade pip not match"
            return render_template('sign_up.html', error_message=error_message)

        user = User(None, name, username, email, password)
        repository.add(user)

        user_created = True
        return render_template('sign_up.html', user_created=user_created)
    
    # If none of the conditions are met, the function will return the default response 
    return render_template('sign_up.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    error = None
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if user_repository.check_password(email, password):
            user = user_repository.get_by_email(email)
            # Set the user ID in session
            session['user_id'], session['logged_in'] = user.id, True
            success_message = 'You were successfully logged in'
            return render_template('login.html', success_message=success_message)
        else:
            error_message = 'Invalid credentials'
            return render_template('login.html', error_message=error_message)
    else:
        if session.get('logged_in'):
            return redirect(url_for('get_index'))
        return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('index.html', logged_in = False)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

@app.route('/new_listing', methods = ['GET','POST'])
def add_new_listing():
    
    if request.method == "GET":
        return render_template('listings/new_listing.html')
    else:
        connection = get_flask_database_connection(app)
        repository = ListingRepository(connection)

        listing_created = False

        user_id = 1
        price = request.form['price_per_night']
        name = request.form['name']
        description = request.form['description']
        
        repository.add(user_id, price, name, description)

        listing_created = True

        if listing_created == True:
            return render_template('listings/index.html')
        else:
            return render_template('listings/new_listing.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
