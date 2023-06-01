import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

from lib.listing_repository import ListingRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    listings = repository.all()
    return render_template('index.html', listings = listings)

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/create')
def create_space():
    return render_template('create.html')

@app.route('/signup')
def get_signup():
    return render_template('signup.html')


app.secret_key = 'your very secret key'

# This route simply returns the login page
# @app.route('/login', methods=['GET'])
# def login():
#     return render_template('login.html')


# @app.route('/login', methods=['POST'])
# def login_post():
#     print("fired")
#     connection = get_flask_database_connection(app)
#     username = request.form['username']
#     password = request.form['password']
#     repo = UserRepository(connection)
#     print(repo.check_password(username, password))
#     if repo.check_password(username, password) == True:
#         print("fired")
#     #     user = UserRepository.find_by_email(email)
#     #     # Set the user ID in session
#         session['user_id'] = username
#         user = username
#         return render_template('login_success.html', user=user)
#     else:
#         return render_template('login_error.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
