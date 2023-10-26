import os
from flask import Flask, request, render_template, redirect, redirect
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.space_parameters_validator import *
from lib.userRepository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# index page
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# regsiter
@app.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def register():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    firstName = request.form['firstName']
    lastName = request.form['lastName']
    password = request.form['password']
    email = request.form['email']

    user = User(None, firstName, lastName, email, password)

    if not user.is_valid():
        return render_template('signup.html', user=user, errors=user.generate_errors())
    
    if repository.accountExists(email):
        return render_template('signup.html', errors='Account already exists with this email')
    
    user = repository.create(user)

    return redirect("/login")

# login
@app.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    email = request.form['useremail']
    password = request.form['password']

    if not repository.accountExists(email) :
        return render_template('login.html', errors='Account does not exist with this email -> Please sign up and try again.')
    
    user = repository.find(email)

    if user.password != password:
        return render_template('login.html', errors='Password is incorrect')
    else:
        return redirect('/spaces') 


# spaces page
@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)
    spaces = repository.all()
    
    return render_template('spaces.html', spaces=spaces)

# individual space page
@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)
    space = repository.find(id)
    
    return render_template('space.html', space=space, id=id)

# get new space
@app.route('/spaces/new', methods=['GET'])
def get_new_space():
    return render_template('new_space.html')


# create new space
@app.route('/spaces', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)

    name = request.form['name']
    description = request.form['description']
    size = request.form['size']
    price = request.form['price']

    validator = SpaceParametersValidator(name, description, size, price)
    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template('/spaces/new', errors=errors)

    space = Space(
        None, 
        validator.get_valid_name(),
        validator.get_valid_description(),
        validator.get_valid_size(),
        validator.get_valid_price(),
        1 #Change last number to owner_id once we have access to current user
    )

    repository.create(space)

    return redirect(f'spaces/{space.id}')


# request to book
@app.route('/requests', methods=['POST'])
def post_request():
    return redirect('/') 

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
