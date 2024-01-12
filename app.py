import os
from flask import Flask, session, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from datetime import datetime
from lib.user import User
from lib.user_repository import UserRepository
from lib.DashboardRepository import DashboardRepository
from lib.RequestRepository import RequestRepository
from lib.Request import Request
from lib.SpacesRepository import SpacesRepository

# test
# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'your_long_and_random_secret_key'
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/',methods=['GET'])
def homepage():
    return redirect('/spaces')

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/log_in', methods=['GET', 'POST'])        
def login():                                         
    if request.method == 'POST':                      
        username = request.form['email'] 
        passw = request.form['passw']  
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        if user_id:=repository.check_valid_login(username,passw):          
            session['email'] = username  
            session['user_id'] = user_id                 
            return redirect('/spaces')
        flash('Email or password is incorrect.','error')
        return render_template('/log_in.html')
    return render_template('/log_in.html')

# @app.route('/log_in', methods=['GET'])
# def login():
    
#     return render_template('log_in.html')

# @app.route('/log_in', methods=['POST'])
# def loginsession():
#     if request.method == 'POST':
#         user = request.form['email']
#         session['user'] = user
#         return redirect('/spaces')
#     return render_template('/log_in.html')
    
#@app.route("/user", methods=['GET'])
#def user():
#    if "email" in session:
#        user = session["email"]
 #       
#        return f"<h1>{user}</h1>"
#    else:
#        return redirect('/log_in')


@app.route('/newspace', methods=['GET'])
def get_new_space():
    try:
        if session['email']:

            connection = get_flask_database_connection(app)
            repository = SpacesRepository(connection)
            spaces = repository.get_by_user(session['user_id'])
            return render_template('newspace.html', username=session['email'],spaces=spaces)
    except:
        return redirect('/spaces')

@app.route('/newspace',methods=['POST'])
def validate_new_space():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    errors = []
    data = [title:=request.form['title'],space_description:=request.form['space_desc'],startdate:=request.form['startdate'],enddate:=request.form['enddate'],price:=request.form['price']]
    if not(all(data)):
        errors.append('One or more fields are blank. Please revise.')
    
        
    try:
        if (datetime.strptime(startdate,'%Y-%m-%d').date() > datetime.strptime(enddate,'%Y-%m-%d').date()) or (datetime.strptime(startdate,'%Y-%m-%d').date() < datetime.now().date()):
            errors.append('Listing must be available from a valid start date.')
    except:
            errors.append('Please enter valid dates')
    
    try:
        price = float(price)
    except:
        errors.append('Please enter a valid price')

    if not(errors):
        try:
            repository.add(title,space_description,price,f'{startdate}-{enddate}',session['user_id'])
            return redirect('/newspace')
        except:
            return redirect('/newspace')
    try:
        spaces = repository.get_by_user(session['user_id'])
        return render_template('newspace.html', errors = errors,username=session['email'],user_id=session['user_id'],spaces=spaces)
    except:
        return render_template('newspace.html')

# POST route for creating new user and password.
@app.route('/signup', methods=['POST'])
def create_user():
    # Set up the database connection and repository
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    # Get the fields from the request form
    email = request.form['email']
    passw = request.form['passw']
    passw_conf = request.form['passw_conf']
    
    if not(repository.check_valid_signup(email)):
        flash("Email already in use.", "error")
        return redirect('/index')

    if passw != passw_conf:
        flash("Passwords must match.", "error")
        return redirect('/index')

    # Create a user object
    user = User(None, email, passw)
    
    user_id = repository.create(user)
    session['email'] = user.email
    session['user_id'] = repository.check_valid_login(email,passw)
    return redirect('/spaces')

@app.route('/spaces', methods=['GET'])
def list_spaces():
    # user_id = session.get('user_id')
    # if user_id is None:
    #     return redirect('/log_in')
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    try:
        if session['email']:
            spaces = repository.get_by_other_users(session['user_id'])
            user_spaces = repository.get_by_user(session['user_id'])
            return render_template('spaces.html', spaces = spaces,signedin =True, username = session['email'], user_spaces=user_spaces)
    except:
        spaces = repository.list_all()
        return render_template('spaces.html',spaces = spaces,signedin =False) 
        

@app.route('/dashboard', methods=['GET', 'POST'])
def get_dashboard():
    connection = get_flask_database_connection(app)
    space_repository = SpacesRepository(connection)
    dash_repository = DashboardRepository(connection)
    try:
        if session['email']:
            user_spaces = space_repository.get_by_user(session["user_id"])
            user_requests = dash_repository.list_req(session["user_id"])
            print('assigns variables')
            user_approvals = dash_repository.list_approvals(session["user_id"]) 
            if request.method == 'POST':
                
                req_id = request.form['req_id']
                space_id = request.form['space_id']
                date_req = request.form['date_req']
                if request.form['approve_or_decline'] == "approve":
                    dash_repository.approve(req_id, space_id, date_req)
                    return redirect('/dashboard')
                if request.form['approve_or_decline'] == "decline":
                    dash_repository.decline(req_id, space_id, date_req)
                    return redirect('/dashboard')
            print('user_spaces = ', user_spaces)
            print('user_requests = ', user_requests)
            print('user_approvals = ', user_approvals)
            return render_template('/dashboard.html', spaces = user_spaces, requests = user_requests, approvals = user_approvals, username = session['email']) 
        
    except:
        return redirect('/spaces') 
    

    
# @app.route('/dashboard', methods=['POST'])
# def post_accept():
#     pass

# @app.route('/dashboard', method=['POST'])
# def post_decline():
#     pass


@app.route('/sign_out')
def logout():
    session.clear()
    return redirect('/spaces')

def formatted_date_range(daterange):
   
    start_date = daterange[0:10]
    end_date = daterange[11:]
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d').strftime('%B %d, %Y')
    
    end_date = datetime.strptime(end_date, '%Y-%m-%d').strftime('%B %d, %Y')
    return f"{start_date} - {end_date}"

@app.route('/requestspace/<int:id>', methods=['GET', 'POST'])
def request_space(id):
    print(f"Received request for /requestspace/{id} with method: {request.method}")
    
    connection = get_flask_database_connection(app)
    spaces_repository = SpacesRepository(connection)
    spaces = spaces_repository.find(id)
    request_repository = RequestRepository(connection)

    if request.method == 'POST':
        print("Processing POST request")
        req_id = session['user_id']
        space_id = id
        date_req = request.form['startdate']
        
              
        request_obj = Request(req_id, space_id, date_req, 'Pending')
        
        request_obj = request_repository.create(request_obj)
        return redirect('/')

    print("Rendering template")
    return render_template('requestspace.html', spaces=spaces, formatted_date_range=formatted_date_range)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

# @app.route('/requestspace', methods=['POST'])
# def send_request():
#     connection = get_flask_database_connection(app)
#     repository = RequestRepository(connection)
#     request = Request [
#         session['user_id'],
        
#     ]
    

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
    

