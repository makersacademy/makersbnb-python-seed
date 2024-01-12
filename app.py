import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.space import *
from lib.user_repository import UserRepository
from lib.user import User
from lib.availability import Availability
from lib.availability_repository import AvailabilityRepository
from datetime import date, timedelta, datetime
from lib.booking import *
from lib.booking_repository import * 

# Create a new Flask app
app = Flask(__name__, static_url_path='/static')
app.secret_key = '1'
users = []
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/home', methods=['GET'])
def get_index():
    if 'user_id' in session:
        user_name = session['user_first_name']
        return render_template('index.html', user_name=user_name, title = "Homepage")
    else:
        return render_template('index.html', title = "Homepage")

@app.route('/template', methods=['GET'])
def get_template():
    return render_template('template.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html', title = "Login Page")

#
@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    existing_user = repository.find_by_email(email)
    if not existing_user:
        return render_template('login.html', error_message="No account has been made with this email. Please sign up.")
    if password == existing_user.password:
        session['user_id'] = existing_user.id
        session['user_email'] = existing_user.email
        session['user_first_name'] = existing_user.first_name
        return redirect(url_for('get_index'))
    else:
        return render_template('login.html', error_message="Incorrect password.", title = "Login Page")
    

@app.route('/logout', methods=['GET'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')
        session.pop('user_email')
    return redirect(url_for('get_index'))

@app.route('/signup', methods=['POST'])
def signup():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    telephone_number = request.form['telephone_number']
    password = request.form['password']
    # Check if the email already exists in the database
    existing_user = repository.find_by_email(email)
    if existing_user:
        return render_template('signup.html', error_message="Email already exists. Please choose a different email.", title = "Sign Up")

    user_id = len(users) + 1
    user = {
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': telephone_number,
        'password': password,
    }
    users.append(user)
    new_user = User(
        id=None,
        first_name=first_name,
        last_name=last_name,
        email=email,
        telephone_number=telephone_number,
        password=password
    )
    repository.create(new_user)
    print(f"User '{email}' signed up with user_id {user_id}.")
    return render_template('signup.html', success_message="Sign-up successful!", title='Signup Page')

@app.route('/signup', methods = ['GET'])
def show_signup():
    return render_template('signup.html', title='Signup Page')

@app.route('/spaces', methods = ['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('spaces.html', spaces = spaces, title = "Spaces")

@app.route('/spaces/<int:id>', methods = ['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    print(repo.find_space_with_availabilities(id))
    if repo.find_space_with_availabilities(id) == None:
        return render_template('no_dates.html')
    space, dates = repo.find_space_with_availabilities(id)
    dates2 = []
    dates = [datetime.strptime(date, "%d-%m-%Y").date() for date in dates]
    for date in dates:
        new_date = date + timedelta(days=1)
        dates2.append(new_date)
    dates = [date.strftime('%d-%m-%Y') for date in dates]
    dates2 = [date.strftime('%d-%m-%Y') for date in dates2]
    return render_template('individual_space.html', space = space, availability = dates, availability2 = dates2, title = f'Spaces - id:{id}')

@app.route('/spaces/<int:id>/filter', methods = ['POST'])
def get_space_by_month(id):
    month = request.form['month-selector']
    print(month)
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    if month == 'show-all':
        return redirect(f'/spaces/{id}')
    if repo.find_space_with_availabilities_month(id, month) == None:
        return render_template('no_dates.html', title = "No dates available")
    space, dates = repo.find_space_with_availabilities_month(id, month)
    dates2 = []
    dates = [datetime.strptime(date, "%d-%m-%Y").date() for date in dates]
    for date in dates:
        new_date = date + timedelta(days=1)
        dates2.append(new_date)
    dates = [date.strftime('%d-%m-%Y') for date in dates]
    dates2 = [date.strftime('%d-%m-%Y') for date in dates2]
    return render_template('individual_space.html', space = space, availability = dates, availability2 = dates2, month = month)

@app.route('/addnewspace', methods = ['GET'])
def add_space_page():
    return render_template('addnewspace.html', title = "Upload a new space")
#
@app.route('/addnewspace', methods = ['POST'])
def add_space():
    connection = get_flask_database_connection(app)
    repo_space = SpaceRepository(connection)
    repo_avaliblity = AvailabilityRepository(connection)
    userid = session.get('user_id')
    if userid is None:
        return redirect('/login')
    name = request.form['name']
    description = request.form['description']
    price = request.form['pricepernight']
    first_date = request.form['availablefrom']
    last_date = request.form['availableto']
    first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
    space = Space(None,int(userid),name,description,int(price))
    space = repo_space.create(space)
    dates = []
    current_date = first_date
    while current_date < last_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    for a_date in dates:
        repo_avaliblity.create(Availability(None, space.id, a_date))
    return redirect('/spaces')

@app.route('/spaces/<int:id>/booking-request', methods = ['POST'])
def bookaspace(id):
    connection = get_flask_database_connection(app)
    first_date = request.form['date-from']
    last_date = request.form['date-to']
    first_date = datetime.strptime(first_date, "%d-%m-%Y").date()
    last_date = datetime.strptime(last_date, "%d-%m-%Y").date() - timedelta(days=1)
    repo_avaliblity = AvailabilityRepository(connection)
    repo_space = SpaceRepository(connection)
    repo_booking = BookingRepository(connection)
    night_ids = repo_avaliblity.find_id(id,first_date,last_date)
    user_id = session.get('user_id')
    status = "pending"
    if 'user_id' in session:
        for index, night_id in enumerate(night_ids):
            if index == 0:
                # Only occurson the first iteration of the loop
                booking_id = repo_booking.create(Booking(None, night_id, user_id, status))
            else:
                repo_booking.create(Booking(None, night_id, user_id, status))
    else:
        return redirect('/login')
    space = repo_space.find(id)
    noofnights = (last_date - first_date).days

    return render_template('bookaspace.html', space = space, date_from = first_date, date_to = last_date + timedelta(days=1), noofnights = noofnights, booking_id = booking_id, title = "Booking Requested")


@app.route('/my-listings', methods = ['GET'])
def get_my_listings():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    if session.get('user_id') == None:
        return redirect('/login')
    spaces = repo.find_by_user(int(session.get('user_id')))
    return render_template('my_listings.html', spaces = spaces, title = "My Listings")

@app.route('/my-profile', methods = ['GET'])
def get_myprofile():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    if session.get('user_id') == None:
        return redirect('/login')
    user = repo.find_user(session.get('user_id'))
    return render_template('my_profile.html', user = user, title = "My profile")

@app.route('/my-requests', methods = ['GET'])
def get_my_requests():
    connection = get_flask_database_connection(app)
    bookings_repository = BookingRepository(connection)
    userid = session.get('user_id')
    requests = bookings_repository.find_all_bookings_and_spaces_by_user_id(userid)

    return render_template('my_requests.html', requests = requests, title = "My requests")

@app.route('/authorization', methods = ['GET'])
def get_authorization():
    error_message = ""
    connection=get_flask_database_connection(app)
    repo_booking = BookingRepository(connection)
    bookings = repo_booking.all()
    booking_status = []
    booking_date = []
    booking_name = []
    booking_id = []
    repo_availability = AvailabilityRepository(connection)
    availability = repo_availability.all()
    repo_spaces = SpaceRepository(connection)
    spaces = repo_spaces.all()
    space_id = 0
    booking_counter = 0
    for booking in bookings:
        try:
            if booking.user_id == session["user_id"]:
                if booking.status != "pending":
                    pass
                else:
                    booking_counter += 1
                    booking_status.append(booking.status)
                    for a in availability:
                        if booking.night_id == a.id:
                            booking_id.append(booking.id)
                            space_id = a.space_id
                            booking_date.append(a.date)
                    for space in spaces:
                        if space_id == space.id:
                            booking_name.append(space.name)
        except:
            error_message = "You need to be logged in to access this page"
    return render_template('authorization.html', names=booking_name, dates=booking_date, status=booking_status, number=booking_counter, error=error_message, booking_id=booking_id)

@app.route('/authorization', methods = ['POST'])
def post_authorization():
    connection=get_flask_database_connection(app)
    repo_booking = BookingRepository(connection)
    button_value = request.form['button_press']
    booking_id = request.form['bookingid']
    repo_booking.update_status(button_value, booking_id)
    return redirect("/authorization")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
