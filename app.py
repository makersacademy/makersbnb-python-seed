import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

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


users = []

@app.route('/signup', methods=['POST'])
def signup():
    # Get user input from the form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    username = request.form['username']
    password = request.form['password']

    # Check if the username already exists
    if any(user['username'] == username for user in users):
        return "Username already exists. Please choose a different username."

    # Generate a simple user_id (replace this with a more robust solution in production)
    user_id = len(users) + 1

    # Store the user's information (replace this with database storage)
    user = {
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number,
        'username': username,
        'password': password,
    }

    users.append(user)

    print(f"User '{username}' signed up with user_id {user_id}.")
    return "Sign-up successful!"

@app.route('/signup')
def show_signup():
    return render_template('signup.html')
    


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
