import os
from datetime import datetime, timedelta
from flask import Flask, request, render_template, redirect, redirect, session, url_for
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.space_parameters_validator import *
from lib.userRepository import UserRepository
from lib.user import User
from lib.unavailable_dates_repository import *
from lib.unavailable_dates import *
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.booking_parameters_validator import BookingParametersValidator
from datetime import timedelta


# Create a new Flask app
app = Flask(__name__)
app.secret_key = "secret"
app.permanent_session_lifetime = timedelta(days=1)

# == Your Routes Here ==

# index page
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)
    spaces = repository.all()

    return render_template('index.html', spaces=spaces)

# filter spaces
@app.route('/', methods=['POST'])
def post_index():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    dates_repository = UnavailableDatesRepository(connection)

    # Get start_date and end_date from the form
    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')

    date_range = []
    current_date = start_date
    while current_date <= end_date:
        date_range.append(current_date.date())
        current_date += timedelta(days=1)
        
    # get only spaces that satisfy the avaialable date range
    spaces = space_repository.all()
    dates = [dates_repository.find_all_unavailable_dates(space.id) for space in spaces]
    
    filtered_ids = list(set([date['space_id'] for lst in dates for date in lst if not date['unavailable_date'] in date_range]))
    
    filtered_spaces = [space_repository.find(id) for id in filtered_ids]

    return render_template('index.html', spaces=filtered_spaces)

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
        session.permanent = True
        session['user'] = email
        return redirect(url_for("get_index"))
    
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

# individual space page
@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app) 
    space_repository = SpaceRepository(connection)
    dates_repository = UnavailableDatesRepository(connection)
    
    space = space_repository.find(id)
    dates = dates_repository.find_all_unavailable_dates(id)
    
    unavailable_dates = [str(date['unavailable_date']) for date in dates]
        
    return render_template('space.html', space=space, id=id, unavailable_dates=unavailable_dates)

# get new space
@app.route('/spaces/new', methods=['GET'])
def get_new_space():
    if "user" in session:      
        return render_template('new_space.html')
    else:
        return (redirect(url_for("login")))


@app.route('/spaces/new', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    dates_repository = UnavailableDatesRepository(connection)
    user_repository = UserRepository(connection)

    name = request.form['name']
    description = request.form['description']
    size = request.form['size']
    price = request.form['price']
    dates = request.form.getlist('unavailable_dates')

    validator = SpaceParametersValidator(name, description, size, price)
    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template('/space.html', errors=errors)
    
    
    if "user" in session:
        email = session["user"]
        owner = user_repository.find(email)

        # since we don't put id when creating space object,
        # we first need to create space and then get the same one from the db
        # with the id, wo we can use it to create date object
        space = Space(
            None, 
            validator.get_valid_name(),
            validator.get_valid_description(),
            validator.get_valid_size(),
            validator.get_valid_price(),
            owner.id
        )

        space_repository.create(space)
        created_space = space_repository.all()[-1]
        
        dates = dates[0].split(",")
        unavailable_dates = [UnavailableDate(created_space.id, date) for date in dates] 

        for unavailable_date in unavailable_dates:
            dates_repository.create(unavailable_date)

        return redirect('/')
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

@app.route('/owners-bookings-dashboard', methods=['GET'])
def get_owners_bookings():
    connection = get_flask_database_connection(app)
    spaceRepository = SpaceRepository(connection)

    if "user" in session:
        user = session["user"]
    else:
        return (redirect(url_for("login")))

    
    id = connection.execute('SELECT id FROM users WHERE email= (%s)', (user,))
    
    id = id[0]['id']
    rows = connection.execute('''
        SELECT bookings.id AS booking_id, bookings.space_id, bookings.booker_id, bookings.start_date, bookings.end_date, bookings.confirmed,
        spaces.id AS space__id, spaces.name, spaces.owner_id, 
        users.id AS user_id, users.first_name, users.last_name, users.email
        FROM bookings 
        JOIN spaces ON bookings.space_id = spaces.id 
        JOIN users ON bookings.booker_id = users.id
        WHERE spaces.owner_id = %s''', (id,))
                              
    bookings = [
        {
            'bookingID':row['booking_id'], 
            'spaceID':row['space_id'], 
            'userID':row['booker_id'],
            'startDate':row['start_date'], 
            'endDate':row['end_date'],
            'confirmed':row['confirmed'], 
            'spaceName':row['name'], 
            'userFirstName':row['first_name'],
            'userLastName':row['last_name'],
            'userEmail':row['email']
        }
        for row in rows
    ]

        
        
    return render_template('ownerbookings.html', bookings=bookings)

@app.route('/process-bookings', methods=['POST'])
def process_bookings():
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)
    
    action = request.form.get('action')
    booking_id  = request.form.get('booking_id')
    
    
    if action == 'Accept':
        repository.update(booking_id, 'confirmed', 'True')
        
    elif action =='Decline':
        repository.delete(booking_id)
        
    
    return redirect(url_for('get_owners_bookings'))
   





# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
