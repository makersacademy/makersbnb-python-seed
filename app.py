import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_class import Space
from lib.space_repository import SpaceRepository
from lib.user_class import User
from lib.user_repository import UserRepository
from datetime import datetime

# Create a new Flask app
app = Flask(__name__)

# Trial Log in account for testing purposes below 
logged_in = None
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    allspaces=spacerepo.all()
    return render_template('index.html',spaces=allspaces)

@app.route('/login')
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    global logged_in
    user_repo = UserRepository(get_flask_database_connection(app))
    username = request.form['Username']
    password = request.form['Password']
    current_user = user_repo.find_by_username(username)
    if current_user==None:
        return render_template('login.html',errors='errors')
    if current_user.password == password:
        logged_in = current_user
        return redirect('/')
    else:
        return render_template('login.html',errors='errors')

@app.route('/register')
def get_register():
    return render_template('register.html')

@app.route('/spaces/new')
def get_new_space():
    global logged_in
    if logged_in != None:
        return render_template('new_space.html')
    if logged_in == None:
        return render_template('need_login.html')

@app.route('/spaces/new', methods=['POST'])
def post_new_space():
    global logged_in
    spaces_repo = SpaceRepository(get_flask_database_connection(app))
    name = request.form['name']
    description = request.form['Description']
    ppn = request.form['Price per night']
    host_id = logged_in.id
    spaces_repo.create(name, host_id, description, ppn)
    return redirect('/')


# This loads t
@app.route('/spaces/<id>')
def get_space(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    SingleSpace=spacerepo.find_by_id(id)
    unavailable_dates=spacerepo.unavailable_days(id)
    return render_template('space_by_id.html',current_date=datetime.now(),space=SingleSpace,unavailable_dates=unavailable_dates)

@app.route('/spaces/<id>', methods=['POST'])
def request_sapce(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    SingleSpace=spacerepo.find_by_id(id)
    date = request.form['date']
    spacerepo.request_a_stay(date,id,logged_in.id)
    return redirect('/')

@app.route('/requests')
def get_requests():
    global logged_in
    if not hasattr(logged_in, '__dict__'):
        return render_template('need_login.html')
    else:
        userrepo = UserRepository(get_flask_database_connection(app))
        requestlist = userrepo.show_bookings(False,logged_in.id)
        return render_template('all_requests.html',user=logged_in,pending_requests=requestlist)

############# CURRENTLY WORKING ON THIS BIT ####
@app.route('/requests/<BOOKINGID>', methods=['POST'])
def approve_request():
    status = request.form['status']
    return status


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
