import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.property_repository import PropertyRepository
from lib.UserRepository import UserRepository
from lib.booking_repository import BookingRepository  
from lib.booking import Booking
from lib.User import User
from datetime import date
from lib.property import Property


# Create a new Flask app
app = Flask(__name__)
app.secret_key = "key"


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    session['user_id'] = None
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def user_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    user = repository.find_by_email(email)
    if user.id == None:
        return render_template('index.html', errors = "User does not exist") , 400
    if password == user.password:
        session['user_id'] = user.id 
        return redirect(f"/listings")
    else:
        return render_template('index.html', errors = "Incorrect password. Please try again.") , 400

@app.route('/sign-up')
def get_sign_up():
    session['user_id'] = None
    return render_template('sign-up.html')

@app.route('/sign-up', methods=['POST'])
def post_create_new_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = User(
        None,
        email = request.form['email'],
        password = request.form['password']
    )
    if user.password == "":
        return render_template('sign-up.html', error_password = True) , 400
    find_user = user_repository.find_by_email(user.email)
    if find_user.id != None:
        return render_template('sign-up.html', errors = True) , 400
    else:
        user_repository.create(user)
        return redirect(f"/index")

@app.route('/listings')
def get_listings():
    if session.get('user_id') == None :
        return redirect(f"/index")
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return render_template('listings.html', properties=properties)

@app.route('/listings/<id>')
def get_listings_id(id):
    if session.get('user_id') == None :
        return redirect(f"/index")
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    property = repository.find(id)
    formatted_price = repository.price_formatter(property)
    return render_template('listings_id.html', property=property, formatted_price=formatted_price)

@app.route('/list-property', methods=['GET'])
def get_list_property():
    if session.get('user_id') == None :
        return redirect(f"/index")
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    if user.id != None:
        return render_template('list-property.html')
    
@app.route('/list-property', methods=['POST'])
def post_new_property():
    current_user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    repo = PropertyRepository(connection)
    name = request.form["name"]
    description = request.form["description"]
    price = request.form["price"]
    list_of_properties = [name, description, price]
    if None in list_of_properties or "" in list_of_properties:
        return render_template('list-property.html', errors="Please fill in all the details."), 400
    else:
        property = Property(None, name, description, price, current_user_id)
        property = repo.create(property)
        return redirect(f"/listings")

@app.route('/logout')
def get_logout():
    return redirect(f"/index")

@app.route('/listings/<property_id>', methods=['POST'])
def book_property(property_id):
    user_id = session.get('user_id') #We get the logged in user id
    connection = get_flask_database_connection(app)
    start_date = request.form["start_date"]
    date_type_start_date = date.fromisoformat(start_date) #We convert the dates entered in the form to date format
    end_date = request.form["end_date"]
    date_type_end_date = date.fromisoformat(end_date)
    booking_repository = BookingRepository(connection)
    property_repository = PropertyRepository(connection)
    property = property_repository.find(property_id)
    formatted_price = property_repository.price_formatter(property)
    booking_date_formatted = Booking(None, date_type_start_date, date_type_end_date, property_id, user_id)
    booking = Booking(None, start_date, end_date, property_id, user_id)
    if not booking.is_valid():
        error = booking.generate_errors()
        return render_template('listings_id.html', error=error, property=property, formatted_price=formatted_price)
    error = "Property is unavailable for those dates"
    confirmation = "Booking confirmed"

    if booking_repository.availability_checker(booking_date_formatted) == False:
        return render_template('listings_id.html', error=error, property=property, formatted_price=formatted_price)
    else:
        booking_repository.create(booking_date_formatted)
        return render_template('listings_id.html', confirmation=confirmation, property=property, formatted_price=formatted_price)
    
@app.route('/my-listings')
def get_my_listings():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    error = "You have no listings to view"
    if user_id:
        current_user_properties = repository.find_property_user_id(user_id)
        if current_user_properties == []:
                    return render_template(
                        'my-listings.html', error=error, properties=current_user_properties)
        else:
            for property in current_user_properties:
                property.price = repository.price_formatter(property)
            return render_template('my-listings.html', properties=current_user_properties)

@app.route('/my-bookings')
def get_my_bookings():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    bookings = booking_repository.find_bookings_with_property_name_and_booking_dates_by_user_id(user_id)
    return render_template('my-bookings.html', bookings=bookings)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
