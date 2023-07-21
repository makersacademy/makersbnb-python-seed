import os
from flask import Flask, request, render_template, redirect, session, url_for, g
from lib.database_connection import get_flask_database_connection
from lib.space_repository import *
from lib.user import *
from lib.user_repository import UserRepository
from lib.request_repository import *
from lib.request import *
# from flask.flask_login import LoginManager
from flask import session


# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# == Your Routes Here ==

def get_logged_in_user_email():
#Session module from Flask, this takes in the email provided in the login function and saves it
    if 'email' in session:
        return f"Logged in as {session['email']}"
    return None

def get_logged_in_user_id():
#Extract user_id from email
    if 'email' in session:
        email = session['email']
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        extract_user = user_repository.find_user(email)
        user_id = extract_user.id
        return user_id
    return None


@app.before_request
def set_logged_in_user():
#The g function saves logged_in_as as a global variable so it doesn't need to be defined in every single route
    g.logged_in_as = get_logged_in_user_email()


@app.before_request
def set_logged_in_user_id():
#Save logged in user_id as global variable
    g.user_id = get_logged_in_user_id()

  
@app.route('/index', methods=['POST'])
def post_user_on_index():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = User(None, request.form['username'], request.form['user_password'], request.form['email'])
    repository.create(user)
    return render_template('spaces/book.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def existing_user_log_in():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user_email = request.form['email']
    user_password = request.form['user_password']

    if repository.username_and_password_match_user(user_email, user_password) == True:
        return redirect('/book_space')
    return "Incorrect username or password. Try Again"


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
# Redirect the user to the homepage or any other page after logout
    return redirect('/index')


@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


@app.route('/book_space', methods = ["GET"])
def get_all_listings():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('/spaces/book.html', spaces=spaces)


@app.route("/spaces/new_space", methods=["GET"])
def get_new_space():
    return render_template("/spaces/new_space.html")


@app.route('/spaces/new_space', methods=["POST"])
def post_new_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    availability = request.form['availability']
    user_id = request.form['user_id']
    new_space = Space(None, name, description, price, availability, user_id)
    repository.create(new_space)
    return redirect(f"/spaces/{new_space.id}")

@app.route('/spaces/<int:id>')
def get_single_space_page(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.find(id)
    space = spaces[0]
    dates = space.availability.split(",")
    return render_template("spaces/select_and_confirm_date.html", space=space, dates=dates)

@app.route('/spaces/<user_id>/my_requests')
def shows_all_requests(user_id):
    connection = get_flask_database_connection(app)
    request_repository = RequestRepository(connection)
    requests = request_repository.find_spaces_by_user_id(user_id)
    requests_made = request_repository.find_requests_sent_by_user_id(user_id)
    return render_template("spaces/list_of_requests_received.html", requests=requests, user_id=user_id, request_made=requests_made)


@app.route('/spaces/<id>/send_booking_request/<date>/')
def confirm_booking_request(id, date):
    connection = get_flask_database_connection(app)
    request_repository = RequestRepository(connection)
    user_id = g.user_id
    request = Request(None, user_id, id, date, "TBC")
    request_repository.create(request)
    return render_template("spaces/confirm_booking.html", request=request)



@app.route('/spaces/<int:id>/send_booking_request/<date>/confirm/<request_id>', methods=["POST"])
def confirm_confirm(id, date, request_id):
    connection = get_flask_database_connection(app)
    request_repository = RequestRepository(connection)
    request_to_use = request_repository.find(request_id)
    request_repository.confirm_booking(request_to_use)
    return render_template("spaces/booking_confirmed.html", request_to_use=request_to_use, id=id, date=date, request_id=request_id)

@app.route('/spaces/<id>/send_booking_request/<date>/decline/<request_id>', methods=["POST"])
def decline_request(id, date, request_id):
    connection = get_flask_database_connection(app)
    request_repository = RequestRepository(connection)
    request_to_use = request_repository.find(request_id)
    request_repository.decline_a_request(request_to_use)
    return render_template("spaces/booking_declined.html", request_to_use=request_to_use, id=id, date=date, request_id=request_id)
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

