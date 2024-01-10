import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.user_repository import UserRepository
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

@app.route('/sign_in', methods=['GET'])
def get_login():
    return render_template('sign_in.html')

@app.route('/sign_in', methods=['POST'])
def get_login_details():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)

    email = request.form['email']
    password = request.form['password']

    if repo.find(email, password):
        user = repo.find_by_email(email)
        return redirect(f"/profile/{user.id}")
    
@app.route('/create_account', methods=['GET'])
def  get_create_account():
    return render_template('create_account.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User(None, username, email, password)
    repo.create(user)
    return redirect(f"/profile/{user.id}")

@app.route('/spaces/<int:id>', methods=['GET'])
def get_space_page(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template("space.html", space=space)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))


