import os
from dotenv import load_dotenv
from flask import Flask, redirect, request, render_template, session
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.request_repository import RequestRepository
from lib.request import Request

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

@app.route('/new-space', methods=["GET"])
def get_space_new():
    if 'user_id' in session:
        return render_template('new-space.html')
    else: 
        return redirect(f"/login")

@app.route('/new-space', methods=["POST"])
def create_space():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    date = request.form['date']
    new_date = date.split(', ')

    space = Space(None, title, description, price, new_date, 1)
    space_repo.create(space)
    return redirect(f"/")

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

@app.route('/spaces/<int:id>', methods=['GET'])
def get_book_page(id):
    if 'user_id' in session:
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        space = repository.find(id)
        return render_template('spaces.html', space=space)
    else:
        return redirect(f"/login")

@app.route('/spaces/<int:id>', methods=['POST'])
def create_request(id):
    connection = get_flask_database_connection(app)
    repository = RequestRepository(connection)
    space_repo = SpaceRepository(connection)
    space = space_repo.find(id)
    selected_date = request.form['date']
    request_obj = Request(None, space.user_id, session['user_id'], id, selected_date, False)
    repository.create(request_obj)
    return redirect(f"/requests")


@app.route('/requests')
def get_requests_page():
    connection = get_flask_database_connection(app)
    repository = RequestRepository(connection)
    space_repo = SpaceRepository(connection)
    spaces = []
    visitors_spaces = []

    if 'user_id' in session:
        owners_requests = repository.get_requests_by_owner_id(session['user_id'])
        visitors_requests = repository.get_requests_by_visitor_id(session['user_id'])
        for request in owners_requests:
            spaces.append(space_repo.find(request.space_id))
        for request in visitors_requests:
            visitors_spaces.append(space_repo.find(request.space_id))
        return render_template('requests.html', owners_requests = owners_requests, spaces = spaces, visitors_spaces = visitors_spaces, visitors_requests = visitors_requests)
    else: 
        return redirect(f"/login")

@app.route('/confirm_request', methods=['POST'])
def confirm_request():
    connection = get_flask_database_connection(app)
    repository = RequestRepository(connection)
    space_repo = SpaceRepository(connection)
    request_id = request.form['confirm']
    repository.confirm(int(request_id))
    request_obj = repository.find(request_id)
    space_repo.remove_date(request_obj.space_id, request_obj.request_date)
    return redirect(f"/requests")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
