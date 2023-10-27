import os
from flask import Flask, request, render_template, redirect, redirect, session, url_for
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.space_parameters_validator import *
from lib.userRepository import UserRepository
from lib.user import User
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.booking_parameters_validator import BookingParametersValidator
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
        email = session["user"]
        return f"<h1>{email}'s profile</h1>"
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
    
# POST /spaces
@app.route('/spaces', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    user_repository = UserRepository(connection)

    name = request.form['name']
    description = request.form['description']
    size = request.form['size']
    price = request.form['price']

    validator = SpaceParametersValidator(name, description, size, price)
    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template('/space.html', errors=errors)

    if "user" in session:
        email = session["user"]
        owner = user_repository.find(email)

        space = Space(
            None, 
            validator.get_valid_name(),
            validator.get_valid_description(),
            validator.get_valid_size(),
            validator.get_valid_price(),
            owner.id
        )

        space_repository.create(space)

        return redirect(f'spaces/{space.id}')
    else:
        return (redirect(url_for("login")))

# POST /bookings
@app.route('/bookings', methods=['POST'])
def create_booking():
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    user_repository = UserRepository(connection)

    space_id = request.form["space_id"]
    dates_list = (request.form["booking_dates"]).split(',')
    start_date = dates_list[0]
    end_date = (dates_list[-1]).strip()

    if "user" in session:
        email = session["user"]
        booker = user_repository.find(email)

        validator = BookingParametersValidator(space_id, start_date, end_date, booker.id)

        if not validator._is_valid():
            errors = validator.generate_errors()
            return redirect(f'/spaces/{space_id}', errors=errors)

        booking = Booking(
            None, 
            validator.get_valid_space_id(),
            booker.id,
            validator.get_valid_start_date(),
            validator.get_valid_end_date(),
            False
        )

        booking_repository.create(booking)

        return redirect(f'/reservations')
    
    else:
        redirect(f'spaces/{space_id}')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
