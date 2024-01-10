import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User, UserRepo
from lib.space import Space
from lib.space_repository import SpaceRepository

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
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new_space.html')

@app.route('/new_space', methods=['POST'])
def create_new_space():
    if 'user_id' not in session:
        return redirect('/')
    
    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    user = user_repo.find_user_by_id(session['user_id'])
    space_name = request.form['space_name']
    description = request.form['description']
    price = request.form['price']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    space_repo = SpaceRepository(connection)
    new_space = Space(None, space_name, description, price, user.id, start_date, end_date)
    space_repo.create(new_space)

    return render_template('spaces.html')

@app.route('/space', methods=['GET'])
def get_space():
    return render_template('space.html')

@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

@app.route('/viewspace/<int:space_id>', methods=['GET'])
def get_viewspace(space_id):
    space_details = space_id  
    if space_details:
        return render_template('request.html', space_details=space_details)
    else:
        # Handle the case where the space with the given ID is not found
        return render_template('error.html', message='Space not found'), 404


@app.route('/list_spaces', methods=['GET'])
def get_list_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('list_spaces.html', spaces=spaces)

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
