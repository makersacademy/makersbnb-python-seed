import os
import datetime
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.spaces import Space
from lib.user_repository import UserRepository
from lib.user import User
from lib.request_repository import RequestRepository
from lib.request import Request

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

    # the following block is horrible. Works mostly. Oh well!
    if len(request.args) == 0 or request.args['start'] == "" or request.args['end'] == "":
        start = datetime.date(2000, 1, 1)
        end = datetime.date(3000, 1, 1)
    else:
        start_list = request.args['start'].split("-")
        start_list = [int(i) for i in start_list]
        end_list = request.args['end'].split("-")
        end_list = [int(i) for i in end_list]
        start = datetime.date(start_list[0], start_list[1], start_list[2])
        end = datetime.date(end_list[0], end_list[1], end_list[2])
    return render_template('spaces.html', spaces=spaces, start=start, end=end)

# Returns page to list a new space
@app.route('/spaces/new', methods=['GET'])
def list_a_space():
    return render_template('space_form.html')

# Adds new space to webpage
@app.route('/spaces', methods=['POST'])
def add_space():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = Space(None, 1, request.form['name'], request.form['description'], request.form['price_per_night'], request.form['start_date'], request.form['end_date']) # id, owner (current user id), name, desc., ppn, active (default: True)
    #if not space.is_valid():
     #   return render_template('space_form.html', space=space, errors=space.generate_errors()), 400
    
    repo.create(space)
    return redirect('/spaces')

# Returns page with space via id
@app.route('/spaces/<id>')
def find_space(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template('spaces_id.html', space=space)

@app.route('/spaces/<id>', methods=['POST'])
def create_request(id):
    connection = get_flask_database_connection(app)
    repo = RequestRepository(connection)
    current_user = 1
    repo.create(Request(current_user, id, request.form['start_date'], request.form['end_date']))
    return redirect('/spaces')

# Returns page with requests made AND requests recieved.
# DO NOT USE
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
