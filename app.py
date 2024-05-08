import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user_repository import UserRepository
from lib.user import User

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

# Returns login page
@app.route('/sessions/new', methods=['GET'])
def get_login():
    return render_template('login.html')

# Returns page with list of all spaces
@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('spaces.html', spaces=spaces)

# Returns page to list a new space
@app.route('/spaces/new', methods=['GET'])
def list_a_space():
    return render_template('space_form.html')

# Adds new space to webpage
@app.route('/spaces', methods=['POST'])
def add_space():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = Space(None, None, request.form['name'], request.form['description'], request.form['price_per_night'], True) # id, owner (current user id), name, desc., ppn, active (default: True)
    if not space.is_valid():
        return render_template('space_form.html', space=space, errors=space.generate_errors()), 400
    
    repo.create(space)
    return render_template('space.html')

# Returns page with space via id
@app.route('/spaces/<id:int>')
def find_space(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template('single_space.html', space=space)

# Returns page with requests made AND requests recieved.
@app.route('/requests')
def get_requests():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    req_made = repo.get_requests_made()
    req_rec = repo.get_requests_recieved()
    return render_template('requests.html', made=req_made, recieved=req_rec)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
