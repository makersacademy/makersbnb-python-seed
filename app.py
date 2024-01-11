import os
import secrets
from flask import Flask, request, render_template, session, redirect

from lib.database_connection import get_flask_database_connection
from lib.user import User, UserRepo
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)



@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")


@app.route("/login", methods=["GET"])
def get_login():
    return render_template("login.html")


@app.route("/spaces", methods=["GET"])
def get_spaces():
    return render_template("spaces.html")
    

@app.route("/space", methods=["GET"])
def get_space():
    return render_template("space.html")

@app.route("/new_space", methods=["GET"])
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

@app.route('/space/<id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    space = space_repo.find_by_id(id)[0]
    return render_template('space.html', space=space)

@app.route('/book/<id>', methods=['POST'])
def book(id):
    connection = get_flask_database_connection(app)
    # space_repo = SpaceRepository(connection)
    # space = space_repo.find_by_id(id)[0]
    user_repo = UserRepo(connection)
    booking_repo = BookingRepository(connection)
    booking_date = request.form['date']
    booking = Booking(None, booking_date, False, session['user_id'], id)
    booking_id = booking_repo.create(booking)
    booking.id = booking_id
    user_repo.add_booking(booking)
    return redirect('/spaces')


@app.route("/requests", methods=["GET"])
def get_requests():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    user_bookings = booking_repo.find_all_by_user(session["user_id"])
    spaces_and_bookings = []
    space_repo = SpaceRepository(connection)
    for booking in user_bookings:
        space = space_repo.find_by_id(booking.space_id)[0]
        spaces_and_bookings.append((booking, space))

    spaces_owned_by_user = space_repo.find_spaces_by_user(session["user_id"])
    owned_space_ids = [space.id for space in spaces_owned_by_user]
    all_bookings = booking_repo.all()
    requests_received = []
    for booking in all_bookings:
        if booking.space_id in owned_space_ids:
            requests_received.append(booking)
    
    user_repo = UserRepo(connection)
    space_bookings_users_rec = []
    for booking in requests_received:
        space = space_repo.find_by_id(booking.space_id)[0]
        user = user_repo.find_user_by_id(booking.user_id)
        space_bookings_users_rec.append((space, booking, user))

    return render_template('requests.html', spaces_and_bookings=spaces_and_bookings, space_bookings_users_rec=space_bookings_users_rec)

  
@app.route("/request", methods=["GET"])
def get_request():
    return render_template("request.html")


@app.route("/logout", methods=["GET"])
def get_logout():
    if "user_id" not in session:
        return redirect("/")
    return render_template("logout.html")
  
  
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


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"].strip().lower()
    password = request.form["password"]

    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    if user_repo.check_password_correct(username, password):
        user = user_repo.find_user_by_username(username)
        session["user_id"] = user.id
        return render_template("spaces.html")
    else:
        return render_template("login.html", errors=["Invalid username or password"])


@app.route("/", methods=["POST"])
def signup():
    username = request.form["username"].strip().lower()
    email = request.form["email"].strip().lower()
    password = request.form["password"]
    password_confirmation = request.form["password-confirmation"]

    errors = []
    if password != password_confirmation:
        errors = ["Password and password confirmation don't match"]

    new_user = User(None, username, email, password, None)
    if not new_user.is_valid():
        errors.append("Invalid Entries")

    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    errors.extend(user_repo.check_user(new_user))
    if errors:
        print(errors)
        return render_template("index.html", errors=errors)
    else:
        # Save the user to the database and then go back to index page
        # Add user to session as logged in
        user_id = user_repo.create_user(new_user)
        session["user_id"] = user_id
        return render_template("spaces.html")


@app.route("/logout", methods=["POST"])
def logout():
    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)

    if user_repo.find_user_by_id(session["user_id"]):
        del session["user_id"]
        return render_template("login.html")
    else:
        return render_template("logout.html", errors=["Nobody logged in"])


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
