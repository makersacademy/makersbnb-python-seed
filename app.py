import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__, static_url_path='/static')

users = []
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
# @app.route('/index', methods=['GET'])
# def get_index():
#     return render_template('index.html')

@app.route('/spaces', methods=['GET'])
def get_space():
    return render_template('spaces.html')


@app.route('/template', methods=['GET'])
def get_template():
    return render_template('template.html')


@app.route('/addnewspace', methods=['GET'])
def get_addnewspace():
    return render_template('addnewspace.html')


@app.route('/template', methods=['GET'])
def get_template():
    return render_template('template.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    # user input from the form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    telephone_number = request.form['telephone_number']
    password = request.form['password']

    # Check if the email already exists
    if any(user['email'] == email for user in users):
        return render_template('signup.html', error_message="Email already exists. Please choose a different email.")

    user_id = len(users) + 1
    user = {
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'telephone_number': telephone_number,
        'password': password,
    }
    users.append(user)
    print(f"User '{email}' signed up with user_id {user_id}.")
    return render_template('signup.html', success_message="Sign-up successful!")

@app.route('/signup')
def show_signup():
    return render_template('signup.html')

@app.route('/addnewspace')
def get_addnewspace():
    return render_template('addnewspace.html')
    
@app.route('/spaces')
def get_spaces():
    return render_template('spaces.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
