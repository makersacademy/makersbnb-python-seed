import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository

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


@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)

    # Get the fields from the request form
    email = request.form['email']
    password = request.form['password']
    password_confirmation = request.form['password_confirmation']

    # SQL query to check if email already exist as must be unique
    email_check = connection.execute('SELECT * from users WHERE email_address = %s', [email])
    # This if is checking to see if the sql query has found an instance of the email
    # If the email_check has found an entry then it will return an error message regarding email
    if email_check:
        email_error = "Email already registered"
        # Rendering template and returning the error message
        return render_template('home.html', email_error = email_error)
    # This else is if the entered email is not already in the database
    else:
        user = User(None, email, password)
        # This checks to make sure password and password confirmation are identical
        if password == password_confirmation:
            # This checks the users email is not blank and password is valid
            if user.is_valid() == True:
                # Save the user to the database
                user_repository.create(user)
                # Redirect to the login page for the user to sign in
                return redirect('/login')
            else:
                errors = user.generate_errors()
                # This else happens when either the email or password is not valid and returns the errors on the sign up page
                return render_template('home.html', errors = errors)
        else:
            password_error = "Passwords must be indentical"
            # This else happens when the password and password confirmation are not identical and returns errors on the sign up page
            return render_template('home.html', password_error = password_error)

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    connection = get_flask_database_connection(app)

    # Get the fields from the request form
    email = request.form['email']
    password = request.form['password']

    # SQL commamnd to check if the email address is in the databse
    email_check = connection.execute('SELECT * from users WHERE email_address = %s', [email])
    # If email is found
    if email_check:
        # This check to see if the password enetered in the password field is the same as the password in the database
        if password == email_check[0]['password']:
            id = email_check[0]['id']
            # Redirects to the users spaces page using their id 
            return redirect(f"/{id}/spaces")
        else:
            password_error = "Incorrect password, please try again"
            # This else happens when the password is incorrect and returns arros on the login page
            return render_template('login.html', password_error = password_error)
    else:
        email_error = "Email not registered, please sign up"
        # This else happens if the email provided is not found in the database and returns error on login page
        return render_template('login.html', email_error = email_error)

@app.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html')

@app.route('/1/spaces', methods=['POST'])
def post_spaces():
    return render_template('spaces.html')

@app.route('/1/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/1/spaces/new', methods=['POST'])
def create_a_space():
    return render_template('create_space.html')


@app.route('/1/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')


@app.route('/1/requests', methods=['POST'])
def post_requests():
    return render_template('requests.html')


@app.route('/1/spaces/1', methods=(['GET']))  # change 1 to id later
def post_request_space():
    return render_template('single_space.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
