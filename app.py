import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import *
from lib.user_repository import *
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_homepage():
    return render_template('homepage.html')

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    users = repository.all()
    users_string = ''
    for user in users:
        users_string += f'{user.email} - {user.password}\n'
    return users_string

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def user_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    email = request.form['email']
    password = request.form['password']

    

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def add_new_user():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

        # Get the fields from the request form
    email = request.form['email']
    password = request.form['password']

        # Create a book object
    user = User(None, email, password)

        # Check for validity and if not valid, show the form again with errors
    if not user.is_valid():
        return 400

        # Save the book to the database
    user = repository.create(user)

        # Redirect to the book's show route to the user can see it
    return redirect("/users")

# login

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces)

@app.route('/spaces/<int:id>', methods=['GET'])
def get_single_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('space_page.html', space=space)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

