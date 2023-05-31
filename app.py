import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.listing_repository import ListingRepository

# Create a new Flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    connection = get_flask_database_connection(app)
    listing_repository = ListingRepository(connection)
    listings = listing_repository.all()
    return render_template('listings/index.html', listings = listings)

@app.route('/signup')
def get_signup():
    return render_template('sign_up.html')

@app.route('/signup', methods=['POST'])
def add_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    user_created = False

    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    user = User(None, name, username, email, password)
    repository.add(user)

    user_created = True

    return render_template('sign_up.html', user_created=user_created)

@app.route('/new_listing', methods = ['GET','POST'])
def add_new_listing():
    
    if request.method == "GET":
        return render_template('listings/new_listing.html')
    else:
        connection = get_flask_database_connection(app)
        repository = ListingRepository(connection)

        listing_created = False

        user_id = 1
        price = request.form['price_per_night']
        name = request.form['name']
        description = request.form['description']
        
        repository.add(user_id, price, name, description)

        listing_created = True

        if listing_created == True:
            return render_template('listings/index.html')
        else:
            return render_template('listings/new_listing.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
