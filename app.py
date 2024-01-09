import os
from flask import Flask, session, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from datetime import datetime
from lib.user import User
from lib.user_repository import UserRepository

from lib.SpacesRepository import SpacesRepository


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
        session['email'] = username                   
        return redirect('/spaces')
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
    
@app.route("/user", methods=['GET'])
def user():
    if "email" in session:
        user = session["email"]
        
        return f"<h1>{user}</h1>"
    else:
        return redirect('/log_in')


@app.route('/newspace', methods=['GET'])
def get_new_space():
    return render_template('newspace.html')

@app.route('/newspace',methods=['POST'])
def validate_new_space():
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
        connection = get_flask_database_connection(app)
        repository = SpacesRepository(connection)
        repository.add(title,space_description,price,f'{startdate}-{enddate}',1)
    return render_template('newspace.html', errors = errors)

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
    
    if not(repository.check_valid(email)):
        flash("Email already in use.", "error")
        return redirect('/index')

    if passw != passw_conf:
        flash("Passwords must match.", "error")
        return redirect('/index')

    # Create a user object
    user = User(None, email, passw)
    
    user = repository.create(user)
    return redirect('/log_in')

@app.route('/spaces', methods=['GET'])
def list_spaces():
    # user_id = session.get('user_id')
    # if user_id is None:
    #     return redirect('/log_in')
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    spaces = repository.list_all()
    try:
        if session['email']:
        
            return render_template('spaces.html',spaces = spaces,signedin =True, username = session['email'])
    except:
        return render_template('spaces.html',spaces = spaces,signedin =False) 
        

@app.route('/sign_out')
def logout():
    session.clear()
    return redirect('/spaces')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
