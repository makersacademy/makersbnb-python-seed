import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_class import Space
from lib.space_repository import SpaceRepository
from lib.user_class import User
from lib.user_repository import UserRepository
from datetime import datetime, timedelta

# Create a new Flask app
app = Flask(__name__)

# Trial Log in account for testing purposes below 
Mike =User('Mike Jones','Jonesy','Password','mail@gmail.com','07752838475',1)
logged_in = Mike
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001
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

@app.route('/spaces/<id>')
def get_space(id):
    spacerepo = SpaceRepository(get_flask_database_connection(app))
    singlespace = spacerepo.find_by_id(id)
    #This is a list of datetime.date objects
    current_day=datetime.now()
    unavailable_dates = spacerepo.unavailable_days(id)
    end_date = current_day + timedelta(days=365)
    # date_range=create_date_range(start_date, end_date)
    date_range =[]
    while current_day <= end_date:
        date_range.append(current_day.date())
        current_day += timedelta(days=1)
    date_list=[date for date in date_range if date not in unavailable_dates]
    return render_template('space_by_id.html',date_list=date_list,space=singlespace)

@app.route('/spaces/<id>', methods=['POST'])
def request_sapce(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    date = request.form['selected_date']
    spacerepo.request_a_stay(date,id,logged_in.id,'pending')
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

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))