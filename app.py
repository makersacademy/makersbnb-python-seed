import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.userRepository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/signup', methods=['GET'])
def get_signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def register():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    firstName = request.form['firstName']
    lastName = request.form['lastName']
    password = request.form['password']
    email = request.form['email']

    user = User(None, firstName, lastName, email, password)

    if not user.is_valid():
        return render_template('signup.html', user=user, errors=user.generate_errors())
    
    if repository.accountExists(email):
        return render_template('signup.html', errors='Account already exists with this email')
    
    user = repository.create(user)

    return redirect("/login")
    

@app.route('/login', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    email = request.form['useremail']
    password = request.form['password']


    

    if not repository.accountExists(email) :
        return render_template('login.html', errors='Account does not exist with this email -> Please sign up and try again.')
    
    user = repository.find(email)

    if user.password != password:
        return render_template('login.html', errors='Password is incorrect')
    else:
        return render_template('index.html') 

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
