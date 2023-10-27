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
#logged_in = Mike
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
    return render_template('index.html',spaces=allspaces,user=logged_in)

@app.route('/login')
def get_login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    global logged_in
    logged_in=None
    return redirect('/')


@app.route('/login', methods=['POST'])
def post_login():
    global logged_in
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
    
@app.route('/login_needed')
def need_login():
    return render_template('need_login.html')

@app.route('/register')
def get_register():
    #return render_template('register.html')
    global logged_in
    if hasattr(logged_in, '__dict__'):
        return render_template('logged_in.html')
    
    else:
        return render_template('register.html')

@app.route('/register', methods= ['POST'])
def send_register():
    global logged_in
    user_repo = UserRepository(get_flask_database_connection(app))
    username = request.form['Username']
    name = request.form['Name']
    password = request.form['Password']
    password2 = request.form['Password2']
    email = request.form['Email']
    phone_number = request.form['Phone Number']

    if password != password2:
        return render_template ('/register.html',errors ='password error')
    
    elif hasattr(user_repo.find_by_username(username), '__dict__'):
            return render_template ('register.html',errors= 'username error')
        
    else:
        user_repo.create (name, username, password, email, phone_number)
        logged_in = user_repo.find_by_username(username)
        return redirect ('/')



@app.route('/spaces/new')
def get_new_space():
    global logged_in
    if hasattr(logged_in, '__dict__'):
        return render_template('new_space.html')
    else:
        return redirect('/login_needed')

@app.route('/spaces/new', methods=['POST'])
def post_new_space():
    global logged_in
    spaces_repo = SpaceRepository(get_flask_database_connection(app))
    name = request.form['name']
    description = request.form['Description']
    ppn = request.form['Price per night']
    unavailabledates=request.form['unavailable']
    host_id = logged_in.id
    NewSpaceId=spaces_repo.create(name, host_id, description, ppn)
    if unavailabledates != '':
        unavailabledateslist=[x.strip() for x in unavailabledates.split(",")]
        for date in unavailabledateslist:
            spaces_repo.request_a_stay(date,NewSpaceId,logged_in.id,'unavailable') 
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
    return render_template('space_by_id.html',date_list=date_list,space=singlespace, user = logged_in)


@app.route('/spaces/<id>', methods=['POST'])
def request_space(id):
    if hasattr(logged_in, '__dict__'):
        spacerepo=SpaceRepository(get_flask_database_connection(app))
        date = request.form['selected_date']
        spacerepo.request_a_stay(date,id,logged_in.id,'pending')
        return redirect('/')
    else:
        return redirect('/login_needed')

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
        return redirect('/login_needed')
    else:
        userrepo = UserRepository(get_flask_database_connection(app))
        requestlist = userrepo.show_bookings('pending',logged_in.id)
        return render_template('all_requests.html',user=logged_in,pending_requests=requestlist)


@app.route('/approve/<id>/<date>', methods=['POST'])
def approve_request(id, date):
    global logged_in
    if not hasattr(logged_in, '__dict__'):
        return redirect('/login_needed')
    else:
        spacerepo=SpaceRepository(get_flask_database_connection(app))
        spacerepo.change_status('approved', id, date)
        return redirect('/requests')

@app.route('/deny/<id>/<date>', methods=['POST'])
def deny_request(id, date):
    global logged_in
    if not hasattr(logged_in, '__dict__'):
        return redirect('/login_needed')
    else:
        spacerepo=SpaceRepository(get_flask_database_connection(app))
        spacerepo.change_status('denied', id, date)
        return redirect('/requests')
    
@app.route('/submitted_requests')
def see_status_of_submitted_requests():
    if hasattr(logged_in, '__dict__'):
        userrepo=UserRepository(get_flask_database_connection(app))
        pending_requests=userrepo.show_submissions('pending',logged_in.id)
        approved_requests=userrepo.show_submissions('approved',logged_in.id)
        denied_requests=userrepo.show_submissions('denied',logged_in.id)
        return render_template('submitted_requests.html',user=logged_in,pending=pending_requests,approved=approved_requests,denied=denied_requests)
    else:
        return render_template('need_login.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
