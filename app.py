import os
import time
from flask import Flask, flash, request, render_template, session, url_for, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'not so secret key'

# == Define Functions ==

#dictionary to store login attempts
login_attempts = {}

# function to store login attempts
def record_login(username):
    login_attempts.setdefault(username, []).append(time.time())

# Log in rate limit function
def has_exceeded_rate_limit(username):
        max_attempts = 3 #or however many attempts you want
        time_window_size = 600 #10 minutes
        #check presence of username in dict
        if username in login_attempts:
            first_try_time = login_attempts[username][0]
        #check if the time window has been breached
        if time.time() - first_try_time <= time_window_size:
            if len(login_attempts[username]) >= max_attempts:
                return True
        else:
            #reset login attempts if time window expired
            login_attempts[username] = []


# Password is valid function
def password_is_valid(password):
    nums = "1234567890"
    special_char = "!@#$%^&*()-_=+[]{};:,<.>/?`~"
    return len(password) >= 8 and any(char in nums for char in password) and \
            any(char in special_char for char in password)

def username_is_valid(username):
    return 0 < len(username) <= 20 and username.isalpha()


# == Routes ==

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

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
            error_message = "Passwords do not match"
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
        print('POST request')
        email = request.form['email']
        password = request.form['password']

        if user_repository.check_password(email, password):
            user = user_repository.get_by_email(email)
            print('correct details')
            # Set the user ID in session
            session['user_id'], session['logged_in'] = user.id, True
            flash('You were successfully logged in')
            return redirect(url_for('get_index'))
        else:
            error = 'invalid credentials'
            print('invalid details')
            return render_template('login.html', error=error)
    else:
        if session.get('logged_in'):
            return redirect(url_for('get_index'))
        print('GET request')
        return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('index.html', logged_in = False)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
