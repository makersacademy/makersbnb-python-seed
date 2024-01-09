import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
# Create a new Flask app
app = Flask(__name__, static_url_path='/static')

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/template', methods=['GET'])
def get_template():
    return render_template('template.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/signup', methods=['POST'])
def signup():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    # User input from the form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    telephone_number = request.form['telephone_number']
    password = request.form['password']
    
    # Check if the email already exists in the database
    existing_user = repository.find_by_email(email)
    if existing_user:
        return render_template('signup.html', error_message="Email already exists. Please choose a different email.")

    # Continue with user registration if the email is unique
    new_user = User(
        id=None,
        first_name=first_name,
        last_name=last_name,
        email=email,
        telephone_number=telephone_number,
        password=password
    )

    created_user = repository.create(new_user)

    return render_template('signup.html', success_message="Sign-up successful!")

@app.route('/signup')
def show_signup():
    return render_template('signup.html')




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
