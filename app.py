import os
from flask import Flask, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import datetime
from lib.space_repository import SpaceRepository
from lib.spaces import Space
from lib.user_repository import UserRepository
from lib.user import User
from lib.request_repository import RequestRepository
from lib.request import Request


app = Flask(__name__)  # Create a Flask application instance
app.secret_key = 'team_mind'  # Set a secret key for the application 

login_manager = LoginManager()  # Create a LoginManager instance
login_manager.init_app(app)  # Initialize the LoginManager with the Flask application instance

@login_manager.user_loader  # Register a user loader function with the LoginManager
def load_user(user_id):  # Define a function to load a user given a user id
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    user_data = repo.find(user_id)
    if user_data:
        return User(user_data.id, user_data.email, user_data.password)
    return None

#LINK: http://127.0.0.1:5001/login


#-------------------------------------------------LOGIN page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # Retrieve the email from the form data
        password = request.form['password']  # Retrieve the password from the form data
        connection = get_flask_database_connection(app)
        users = UserRepository(connection)
        users2 = users.all()
        for user in users2:  # Iterate over the users dictionary
            if user.email == email and user.password == password:
                user = User(user.id, email, password)
                login_user(user)
                return render_template('dashboard.html', user=user)
        
        return render_template('invalid_login.html')
    
    return render_template('login.html')

#-------------------------------------------------LOGIN page


#------------------------------------------------- DASHBOARD
@app.route('/dashboard')  
@login_required  # Decorate the route to require authentication
def dashboard():  # Define a function to handle requests to the dashboard page
    return render_template("dashboard.html")  # Return a greeting message with the current user's id and email
#------------------------------------------------- DASHBOARD


#-------------------------------------------------------------------- LOGOUT 
@app.route('/logout', methods=['POST'])  
def return_to_login():  
    return render_template('login.html') #Redirect back to login page
#-------------------------------------------------------------------- LOGOUT 


#-------------------------------------------------------------------- Incorrect password page
@app.route('/invalid_login', methods=['POST'])  
def return_to_login_after_incorrect_password():  # Define a function to handle requests to the login page after clicking return to login page
    return render_template("login.html") 
#-------------------------------------------------------------------- Incorrect password page


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
    req_repo = RequestRepository(connection)
    #space_repo = SpaceRepository(connection)
    reqs_from = req_repo.list_request_from_user(1) # replace with current user id
    reqs_to = req_repo.list_request_to_user(1) # replace with current user id
    return render_template('requests.html', reqs_from=reqs_from, reqs_to=reqs_to)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
