import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.space import *
from lib.user_repository import UserRepository
from lib.user import User
from lib.availability import Availability
from lib.availability_repository import AvailabilityRepository
from datetime import date, timedelta, datetime

# Create a new Flask app
app = Flask(__name__, static_url_path='/static')
app.secret_key = '1'
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    if 'user_id' in session:
        user_name = session['user_email']
        return render_template('index.html', user_name=user_name)
    else:
        return render_template('index.html')

@app.route('/spaces', methods=['GET'])
def get_space():
    return render_template('spaces.html')


@app.route('/template', methods=['GET'])
def get_template():
    return render_template('template.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    existing_user = repository.find_by_email(email)
    if not existing_user:
        return render_template('login.html', error_message="No account has been made with this email. Please sign up.")
    if password == existing_user.password:
        session['user_id'] = existing_user.id
        session['user_email'] = existing_user.email
        return redirect(url_for('get_index'))
    else:
        return render_template('login.html', error_message="Incorrect password.")
    

@app.route('/logout', methods=['GET'])
def logout():
    if 'user_id' in session:
        session.pop('user_id')
        session.pop('user_email')
    return redirect(url_for('get_index'))

@app.route('/signup', methods=['POST'])
def signup():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    telephone_number = request.form['telephone_number']
    password = request.form['password']
    # Check if the email already exists in the database
    existing_user = repository.find_by_email(email)
    if existing_user:
        return render_template('signup.html', error_message="Email already exists. Please choose a different email.")

    user_id = len(users) + 1
    user = {
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone_number': telephone_number,
        'password': password,
    }
    users.append(user)
    print(f"User '{email}' signed up with user_id {user_id}.")
    return render_template('signup.html', success_message="Sign-up successful!", title='Signup Page')

    # Continue with user registration if the email is unique
    new_user = User(
        id=None,
        first_name=first_name,
        last_name=last_name,
        email=email,
        telephone_number=telephone_number,
        password=password
    )
    repository.create(new_user)
    return render_template('signup.html', success_message="Sign-up successful!")

@app.route('/signup')
def show_signup():
    return render_template('signup.html', title='Signup Page')

@app.route('/spaces', methods = ['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template('spaces.html', spaces = spaces)


'''
@app.route('/spaces/<int:id>', methods = ['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template {create template for single space page and then finish this}
'''

@app.route('/addnewspace', methods = ['GET'])
def add_space_page():
    return render_template('addnewspace.html')

@app.route('/addnewspace', methods = ['POST'])
def add_space():
    connection = get_flask_database_connection(app)
    repo_space = SpaceRepository(connection)
    repo_avaliblity = AvailabilityRepository(connection)
    userid = request.form['userID']
    name = request.form['name']
    description = request.form['description']
    price = request.form['pricepernight']
    first_date = request.form['availablefrom']
    last_date = request.form['availableto']
    first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
    space = Space(None,int(userid),name,description,int(price))
    space = repo_space.create(space)
    dates = []
    current_date = first_date
    while current_date < last_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    for a_date in dates:
        repo_avaliblity.create(Availability(None, space.id, a_date))
    return redirect('/spaces')



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
