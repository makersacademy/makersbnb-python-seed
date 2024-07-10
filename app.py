import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.listing import Listing
from lib.listing_repository import ListingRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
# @app.route('/index', methods=['GET'])
# def get_index():
#     return render_template('index.html')

# # GET all booking
# @app.route('/booking', methods=['GET'])
# def get_booking():
#     return render_template('booking.html')

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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
