import os
from flask import Flask, request, render_template, url_for, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.listing import Listing
from lib.listing_repository import ListingRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.user import User
from lib.user_repository import UserRepository
from lib.review import Review
from lib.review_repository import ReviewRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/index', methods=['GET'])
def get_homepage():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/listings/new', methods=['GET'])
def get_new_listing():
    return render_template('new_listings.html')

@app.route("/listings", methods=["POST"])
def post_listing():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    
    name = request.form["name"]
    description = request.form["description"]
    price_per_night = request.form["price_per_night"]
    available_from = request.form["available_from"]
    available_to = request.form["available_to"]
    

    listing = Listing(None, name, description, price_per_night, available_from, available_to) 
    listing = repository.create(listing)
    return redirect(f"/listings/{listing.id}")

@app.route("/listings", methods=["GET"])
def show_listings():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listings = repository.all()
    return render_template("listings.html", listings=listings)

@app.route('/listings/<int:id>', methods=['GET'])
def get_listing(id):
        connection = get_flask_database_connection(app)
        repository = ListingRepository(connection)
        listing = repository.find_by_id(id)
        return render_template('single_listing.html', listing=listing)

@app.route('/bookings', methods=['GET'])
def get_bookings():
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)
    bookings = repository.all()
    listing_repository = ListingRepository(connection)
    listings = listing_repository.all()
    listing_names = {listing.id: listing.name for listing in listings}
    return render_template('bookings.html', bookings=bookings, listing_names=listing_names)

@app.route('/bookings/new/<int:listing_id>', methods=['POST'])
def post_booking(listing_id):
    connection = get_flask_database_connection(app)
    repository = BookingRepository(connection)
    user_repository = UserRepository(connection)
    # booker_id = user_repository.find_by_id(session['user_id'])
    booker_id = 1 # hardcoding user id for now
    check_in = request.form['check_in']
    check_out = request.form['check_out']
    booking = Booking(None, listing_id, None, booker_id, check_in, check_out)
    booking = repository.create(booking)
    return redirect('/bookings')

@app.route('/bookings/new/<int:listing_id>', methods=['GET'])
def get_booking_form(listing_id):
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listing = repository.find_by_id(listing_id)
    return render_template('booking_form.html', listing=listing)

@app.route('/listings/review/<int:listing_id>', methods = ['GET'])
def get_review_form(listing_id):
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listing = repository.find_by_id(listing_id)
    return render_template('review_form.html', listing=listing)

@app.route('/listings/review/<int:listing_id>', methods = ['POST'])
def post_review(listing_id):
    
    try: 
        connection = get_flask_database_connection(app)
        repository = ReviewRepository(connection)
        review_text = request.form['review_text']
        rating = request.form['rating']
        review = Review(None, listing_id, review_text, rating)
        review = repository.create(review)
        return redirect('/listings/<int:listing_id>')
    
    except Exception as e:
        print(f'Errors printed here,{e}')
        return redirect('/index')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
