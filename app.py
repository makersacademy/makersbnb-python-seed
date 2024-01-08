import os
from flask import Flask, request, render_template,redirect
from lib.database_connection import get_flask_database_connection

from lib.user import User
from lib.user_repository import UserRepository

from lib.SpacesRepository import SpacesRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/',methods=['GET'])
def homepage():
    return redirect('/index')

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/log_in', methods=['GET'])
def get_login():
    return render_template('log_in.html')


@app.route('/newspace', methods=['GET'])
def get_new_space():
    return render_template('newspace.html')


@app.route('/login', methods=['POST'])
def create_user():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    # Get the fields from the request form
    email = request.form['email']
    passw = request.form['passw']

        # Create a user object
    user = User(None, email, passw)
    
    user = repository.create(user)
    return render_template('log_in.html')

@app.route('/spaces', methods=['GET'])
def list_spaces():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    spaces = repository.list_all()
    return render_template('spaces.html',spaces = spaces)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
