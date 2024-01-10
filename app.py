import os
from flask import Flask, request, render_template, redirect, session 
from lib.database_connection import get_flask_database_connection
from lib.user import *
from lib.user_repository import *
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = '20240110'

# == Your Routes Here ==

@app.route('/', methods=['GET']) #To-Do integrate def home into def get_homepage
# def home():
    # if "username" in session:
    #     return f"Logged in as {session['username']}"
    # return "You are not logged in"
def get_homepage():
    return render_template('homepage.html')

@app.route('/users', methods=['GET'])
def get_users():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    users = repository.all()
    users_string = ''
    for user in users:
        users_string += f'{user.email} - {user.password}\n'
    return users_string

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def user_login():
    # connection = get_flask_database_connection(app)
    # repository = UserRepository(connection)
    # session['email'] = request.form['email']
    return redirect("/spaces")

# @app.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     if 'username' in session:
#         username = session['username']
#         return render_template('dashboard.html', username=username)
#     else:
#         return redirect(url_for('login'))

@app.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def add_new_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    email = request.form['email']
    password = request.form['password']

    user = User(None, email, password)

    if not user.is_valid():
        return 400

    user = repository.create(user)
    session['email'] = request.form['email']
    return redirect("/spaces")

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    
    # email = session['email']
    return render_template('spaces.html', spaces=spaces)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

