import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)
# global variable 
id = 1

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # to check if login information is valid we'll need user.py     
    return render_template('login.html')

@app.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html')

@app.route('/1/spaces', methods=['POST'])
def post_spaces():
    return render_template('spaces.html')

@app.route('/1/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html' )

@app.route('/1/spaces/new', methods=['POST'])
def create_a_space():
    return render_template('create_space.html')

@app.route('/1/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

@app.route('/1/requests', methods=['POST'])
def post_requests():
    return render_template('requests.html')


@app.route('/1/spaces/1' , methods=(['GET']))  #change 1 to id later
def post_request_space():
    return render_template('single_space.html')

    




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
