import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# home page
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# create an account
@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    return render_template('signup.html')


# login
@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    return render_template('login.html')

# spaces page
@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)
    spaces = repository.all()
    
    return render_template('spaces.html', spaces=spaces)

# individual space page
@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)
    space = repository.find(id)
    
    return render_template('space.html', space=space, id=id)


# new space page
@app.route('/spaces/new', methods=['GET'])
def new_space():    
    return render_template('new_space.html')


# requests page
@app.route('/requests', methods=['GET'])
def get_requests():
    connection = get_flask_database_connection(app) 
    repository = SpaceRepository(connection)
    
    requested_spaces = [repository.find(1)]
    received_spaces = [repository.find(2)]
    
    return render_template('requests.html', requested_spaces=requested_spaces, received_spaces=received_spaces)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
