import os
from flask import Flask, request, render_template
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
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET all listings
@app.route('/listings', methods=['GET'])
def get_listings():
    return render_template('listings.html')

# GET all booking
@app.route('/booking', methods=['GET'])
def get_booking():
    return render_template('booking.html')

@app.route("/listings", methods=["POST"])
def post_listing():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listing = Listing(None, request.form["name"], request.form["description"], request.form["price_per_night"], request.form["available_from"], request.form["available_to"])
    listing = repository.create(listing)
    return "Listing added!", 200


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
