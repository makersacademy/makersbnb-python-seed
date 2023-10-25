import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.spaces_repository import SpacesRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET /listings return the listing of all the spaces
@app.route('/listings', methods=['GET'])
def get_listings():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    all_spaces = repository.all_listings()
    print("test")
    print(all_spaces[0].name)
    return render_template('listings.html', all_spaces=all_spaces)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

# @app.route('/login', methods=['GET']) 
# def get_login():
#     return render_template('login.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/listings', methods=['POST'])
def post_new_listing():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    name = request.form['name']
    description = request.form['description']
    listing = Space(None, name, description, price, date_from, date_to)
    repository.create_listing(listing)
    return redirect('/listings')

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
