import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User, UserRepo

app = Flask(__name__)
app.secret_key='12'

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/new_space', methods=['GET'])
def get_new_space():
    return render_template('new_space.html')

@app.route('/space', methods=['GET'])
def get_space():
    return render_template('space.html')

@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

@app.route('/request', methods=['GET'])
def get_request():
    return render_template('request.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'].strip().lower()
    password = request.form['password']

    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    if user_repo.check_password_correct(username, password):
        user = user_repo.find_user_by_username(username)
        session['user_id'] = user.id
        return render_template('spaces.html')
    else:
        return render_template('login.html', errors=['Invalid username or password'])


@app.route('/', methods=['POST'])
def signup():
    username = request.form['username'].strip().lower()
    email = request.form['email'].strip().lower()
    password = request.form['password']
    password_confirmation = request.form['password-confirmation']

    errors = []
    if password != password_confirmation:
        errors = ["Password and password confirmation don't match"]
    
    new_user = User(None, username, email, password, None)
    if not new_user.is_valid():
        errors.append('Invalid Entries')

    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    errors.extend(user_repo.check_user(new_user))
    if errors:
        print(errors)
        return render_template('index.html', errors=errors)
    else:
        # Save the user to the database and then go back to index page
        # Add user to session as logged in
        user_id = user_repo.create_user(new_user) 
        session['user_id'] = user_id
        return render_template('spaces.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
