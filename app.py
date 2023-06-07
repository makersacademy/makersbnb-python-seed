import os
from dotenv import load_dotenv
from flask import Flask, redirect, request, render_template, session
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.space_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# == Your Routes Here ==

# GET /home
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    logged_in = False
    if 'user_id' in session:
        logged_in = True
    spaces = space_repo.all()
    return render_template('home.html', spaces = spaces, logged_in=logged_in)

@app.route('/signup', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    user = User(None, first_name, last_name, email, password)
    if not user.is_valid():
        errors = user.generate_errors()
        return render_template("sign_up.html", errors=errors)
    user_repository = UserRepository(connection)
    user = user_repository.create_user(user)
    session['user_id'] = user.id
    return redirect(f"/")

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect(f"/")

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    user_repository = UserRepository(connection)
    if user_repository.check_password(email, password):
        user = user_repository.find_user_by_email(email)
        session['user_id'] = user.id
        return redirect(f"/")
    else:
        return render_template('login.html', errormessage="Invalid email or password")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
