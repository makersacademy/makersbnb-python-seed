import os
from flask import Flask, request, render_template, session, redirect
from lib.user_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from dotenv import load_dotenv
from lib.listing_repository import ListingRepository
from jinja2 import Environment, FileSystemLoader

load_dotenv()

# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

env = Environment(
    loader=FileSystemLoader("templates/"),
    autoescape=True
)
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    if 'user_id' not in session:
        template = env.get_template('index.html.jinja2')
        return render_template(template)
    else:
        return redirect('/account_page')

@app.route('/', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    user_name = request.form['user_name']
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    repository.create(email, password, user_name)
    return redirect("/login")

@app.route('/login', methods=['GET'])
def get_login():
    template = env.get_template('login.html.jinja2')
    return render_template(template)

@app.route('/login', methods=['POST'])
def post_login():
    email = request.form['email']
    password_attempt = request.form['password']
    valid_password = None
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if repository.check_password(email, password_attempt):
        user = repository.find_by_email(email)
        session['user_id'] = user.id
        session['user_name'] = user.user_name
        return redirect('/account_page')
    else:
        valid_password = False
        template = env.get_template('login.html.jinja2')
        return render_template(template, valid_password = valid_password)
    
@app.route('/signout')
def get_signout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    return redirect('/')

@app.route('/account_page')
def account_page():
    if 'user_id' not in session:
        # No user id in the session so the user is not logged in.
        return redirect('/login')
    else:
        # The user is logged in, display their account page.
        connection = get_flask_database_connection(app)
        repository = ListingRepository(connection)
        listings = repository.find_by_user(session['user_id'])
        user_name = session['user_name']
        template = env.get_template('account_page.html.jinja2')
        return render_template(template, listings = listings, user_name = user_name)
    
@app.route('/list_space')
def list_space():
    template = env.get_template('list_space.html.jinja2')
    return render_template(template)

@app.route('/list_space', methods=['POST'])
def list_new_space():
    name = request.form['name']
    description = request.form['description']
    cost = request.form['cost']
    user_id = session['user_id']
    connection = get_flask_database_connection(app)
    repository = ListingRepository(connection)
    repository.create(name,description,cost,user_id)
    return redirect("/account_page")




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
