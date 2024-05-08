import os
from flask import Flask, request, render_template, redirect, flash, jsonify, url_for
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User

# from datetime import datetime


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

# open sign up page
@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")

# submit sign up info
@app.route('/signup', methods = ['POST'])
def sign_up_form():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)

    # check validation
    if not has_valid_data(request.form, connection):
            return "error: inputs not valid", 400
    
    # read form data to generate new record for "users" table
    save_username = request.form.get('username')
    save_user_passwor = request.form.get('user_password')
    save_email = request.form.get('email')
    save_full_name = request.form.get('full_name')
    
    new_user = User(None, save_username, save_user_passwor, save_email, save_full_name)
    repo.add_user(new_user)

    return redirect(url_for("get_index"))

def has_valid_data(form, connection):
    handle = form['username']
    email = form['email']
    password = form['user_password']
    repo = connection.execute("SELECT * FROM users WHERE username = %s OR email = %s", [handle, email])

    if repo != []:
        return handle not in repo[0]['username'] and \
            email not in repo[0]['email'] and \
            len(password) >= 8 and \
            any(char in 'qwertyuiopasdfghjklzxcvbnm' for char in password) and \
            any(char in 'QWERTYUIOPASDFGHJKLZXCVBNM,' for char in password) and \
            any(char in '!@£$%^&*//.,' for char in password) and \
            any(char in '1234567890' for char in password)
    return len(password) >= 8 and \
        any(char in 'qwertyuiopasdfghjklzxcvbnm' for char in password) and \
        any(char in 'QWERTYUIOPASDFGHJKLZXCVBNM,' for char in password) and \
        any(char in '!@£$%^&*//.,' for char in password) and \
        any(char in '1234567890' for char in password)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
