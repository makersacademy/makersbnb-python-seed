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

#Magicman = User(1,'Magicman','magic man', '782993a','Macicman@hotmail.com','01214960879')
#logged_in = Magicman

logged_in = None
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
    user_repo = UserRepository(get_flask_database_connection(app))
    username = request.form['Username']
    password = request.form['Password']
    current_user = user_repo.find_by_username(username)
    if not hasattr(current_user, '__dict__'):
        return render_template('login.html',errors='errors')
    if current_user.password == password:
        logged_in = current_user
        return redirect('/')
    else:
        return render_template('login.html',errors='errors')

@app.route('/register')
def get_register():
    #return render_template('register.html')

    if logged_in != None:
        return render_template('logged_in.html')
    
    if logged_in == None:
        return render_template('register.html')

@app.route('/register', methods= ['POST'])
def send_register():
    user_repo = UserRepository(get_flask_database_connection(app))
    name = request.form['Username']
    username = request.form['Name']
    password = request.form['Password']
    email = request.form['Email']
    phone_number = request.form['Phone Number']
    user_repo.create (username, name, password, email, phone_number)
    return redirect ('/')



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
    NewSpaceId=spaces_repo.create(name, host_id, description, ppn)
    unavailabledateslist=[x.strip() for x in (request.form['unavailable']).split(",")]
    for date in unavailabledateslist:
        spaces_repo.request_a_stay(date,NewSpaceId,logged_in.id,True) 
    return redirect('/')

@app.route('/spaces/<id>')
def get_space(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    SingleSpace=spacerepo.find_by_id(id)
    unavailable_dates=spacerepo.unavailable_days(id)
    return render_template('space_by_id.html',current_date=datetime.now(),space=SingleSpace,unavailable_dates=unavailable_dates,user=logged_in)

@app.route('/spaces/<id>', methods=['POST'])
def request_space(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    SingleSpace=spacerepo.find_by_id(id)
    date = request.form['date']
    spacerepo.request_a_stay(date,id,logged_in.id,False)
    return redirect('/')

@app.route('/spaces/<id>/delete')
def delete_space(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    spacerepo.delete_by_id(id)
    print (f'Deleted space with id {id}')
    return redirect('/')

@app.route('/spaces/<id>/unavailable', methods=['POST'])
def mark_date_as_unavailable(id):
    spacerepo=SpaceRepository(get_flask_database_connection(app))
    unavailabledateslist=[x.strip() for x in (request.form['unavailable']).split(",")]
    for date in unavailabledateslist:
        spacerepo.request_a_stay(date,id,logged_in.id,'unavailable') 
    return redirect(f'/spaces/{id}')

@app.route('/requests')
def get_requests():
    global logged_in
    if not hasattr(logged_in, '__dict__'):
        return render_template('need_login.html')
    else:
        userrepo = UserRepository(get_flask_database_connection(app))
        requestlist = userrepo.show_bookings('pending',logged_in.id)
        return render_template('all_requests.html',user=logged_in,pending_requests=requestlist)


@app.route('/approve/<id>/<date>', methods=['POST'])
def approve_request(id, date):
    global logged_in
    if not hasattr(logged_in, '__dict__'):
        return render_template('need_login.html')
    else:
        spacerepo=SpaceRepository(get_flask_database_connection(app))
        spacerepo.change_status('approved', id, date)
        return redirect('/requests')

@app.route('/deny/<id>/<date>', methods=['POST'])
def deny_request(id, date):
    global logged_in
    if not hasattr(logged_in, '__dict__'):
        return render_template('need_login.html')
    else:
        spacerepo=SpaceRepository(get_flask_database_connection(app))
        spacerepo.change_status('denied', id, date)
        return redirect('/requests')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

