import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.sign_up import *

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
