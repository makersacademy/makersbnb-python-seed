import os
from flask import Flask, request, render_template, redirect, redirect, session, url_for
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.space_parameters_validator import *
from lib.userRepository import UserRepository
from lib.user import User
from datetime import timedelta


# Create a new Flask app
app = Flask(__name__)
app.secret_key = "secret"
app.permanent_session_lifetime = timedelta(days=1)

# == Your Routes Here ==

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

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
        session.permanent = True
        session['user'] = email
        return redirect(url_for("get_spaces"))
    
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for("login"))

@app.route('/profile')
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}'s profile</h1>"
    else:
        return (redirect(url_for("login")))
    
# GET /
# Returns the homepage
# Try it:
#   ; open http://localhost:5000
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

# GET /spaces/new
# Returns the new space page with a form to add a space
# Try it:
#   ; open http://localhost:5000/spaces/new
@app.route('/spaces/new', methods=['GET'])
def get_new_space():
    if "user" in session:      
        return render_template('new_space.html')
    else:
        return (redirect(url_for("login")))
    
# POST /
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/
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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
