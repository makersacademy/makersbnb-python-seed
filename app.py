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
    if 'user_id' in session:
        return redirect('/list_spaces')
    return render_template("index.html")


@app.route("/login", methods=["GET"])
def get_login():
    if 'user_id' in session:
        return redirect('/list_spaces')
    return render_template("login.html")


@app.route("/new_space", methods=["GET"])
def get_new_space():
    if "user_id" not in session:
        return redirect("/")
    return render_template("new_space.html", user=show_user())


@app.route("/new_space", methods=["POST"])
def create_new_space():
    if "user_id" not in session:
        return redirect("/")

    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    user = user_repo.find_user_by_id(session["user_id"])
    space_name = request.form["space_name"]
    location = request.form["location"]
    description = request.form["description"]
    price = request.form["price"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    space_repo = SpaceRepository(connection)
    new_space = Space(
        None, space_name, location, description, price, user.id, start_date, end_date
    )
    space_repo.create(new_space)
    all_spaces = space_repo.all()

    return render_template("list_spaces.html", spaces=all_spaces, user=show_user())


@app.route("/space/<space_id>", methods=["GET"])
def get_space(space_id):
    if "user_id" not in session:
        return redirect("/")

    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    space = space_repo.find_by_id(space_id)[0]
    return render_template("space.html", space=space, user=show_user())


@app.route("/book/<id>", methods=["POST"])
def book(id):
    if "user_id" not in session:
        return redirect("/")
    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    booking_repo = BookingRepository(connection)
    space_repo = SpaceRepository(connection)
    space = space_repo.find_by_id(id)[0]
    booking_date = request.form["date"]
    booking = Booking(None, booking_date, False, False, session["user_id"], id)
    if booking_repo.already_booked(booking):
        return render_template(
            "/booking_failed.html", id=id, error="Booking already taken", user=show_user()
        )
    if not space_repo.space_available(booking_date, space):
        return render_template(
            "/booking_failed.html", id=id, error="Space not available on this date", user=show_user()
        )
    booking_id = booking_repo.create(booking)
    booking.id = booking_id
    user_repo.add_booking(booking)
    return redirect("/requests")


@app.route("/requests", methods=["GET"])
def get_requests():
    if "user_id" not in session:
        return redirect("/")

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

    return render_template(
        "requests.html",
        spaces_and_bookings=spaces_and_bookings,
        space_bookings_users_rec=space_bookings_users_rec,
        user=show_user()
    )


@app.route("/logout", methods=["GET"])
def get_logout():
    if "user_id" not in session:
        return redirect("/")
    return render_template("logout.html", user=show_user()) # CHECK THIS LINE TOMORROW


@app.route("/viewspace/<int:space_id>", methods=["GET"])
def get_viewspace(space_id):
    if "user_id" not in session:
        return redirect("/")

    space_details = space_id
    if space_details:
        return render_template("request.html", space_details=space_details, user=show_user())
    else:
        # Handle the case where the space with the given ID is not found
        return render_template("error.html", message="Space not found", user=show_user()), 404

def show_user():
    if "user_id" in session:
        connection = get_flask_database_connection(app)
        user_repo = UserRepo(connection)
        user = user_repo.find_user_by_id(session["user_id"])
        return user
    return None

@app.route("/list_spaces", methods=["GET", "POST"])
def spaces():
    if "user_id" not in session:
        return redirect("/")
    if request.method == "GET":
        return render_template("list_spaces.html", user=show_user())
    elif request.method == "POST":
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        if "available_from" in request.form and "available_to" in request.form:
            available_from = request.form["available_from"]
            available_to = request.form["available_to"]
            spaces = repository.get_available_spaces(available_from, available_to)
            if not spaces or spaces == "No results found":
                return render_template("list_spaces.html", spaces=[], no_results=True, user=show_user())
            else:
                return render_template("list_spaces.html", spaces=spaces, user=show_user())
    return render_template("list_spaces.html", user=show_user())


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"].strip().lower()
    password = request.form["password"]
    if not username or not password:
        return render_template("login.html", errors=["Invalid username or password"],user=show_user())

    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    if user_repo.check_password_correct(username, password):
        user = user_repo.find_user_by_username(username)
        session["user_id"] = user.id
        return redirect("/list_spaces")
    else:
        return render_template("login.html", errors=["Invalid username or password"],user=show_user())


@app.route("/", methods=["POST"])
def signup():
    username = request.form["username"].strip().lower()
    email = request.form["email"].strip().lower()
    password = request.form["password"]
    password_confirmation = request.form["password-confirmation"]

    errors = []
    if password != password_confirmation:
        errors = ["Password and password confirmation don't match"]
    print(username, email, password, password_confirmation)
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
        return redirect("/list_spaces")


@app.route("/request/<id>", methods=["GET"])
def get_request(id):
    if "user_id" not in session:
        return redirect("/")

    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    user_repo = UserRepo(connection)
    booking_repo = BookingRepository(connection)
    booking = booking_repo.find(id)
    space = space_repo.find_by_id(booking.space_id)[0]
    user = user_repo.find_user_by_id(booking.user_id)
    return render_template("request.html", booking=booking, space=space, user=user)


@app.route("/approve/<id>", methods=["POST"])
def approve(id):
    if "user_id" not in session:
        return redirect("/")

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.confirm(id)
    return redirect("/requests")


@app.route("/reject_request/<id>", methods=["POST"])
def reject_request(id):
    if "user_id" not in session:
        return redirect("/")

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.reject(id)
    return redirect("/requests")


@app.route("/delete_request/<id>", methods=["POST"])
def delete_request(id):
    if "user_id" not in session:
        return redirect("/")

    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.delete(id)
    return redirect("/requests")


@app.route("/logout", methods=["POST"])
def logout():
    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)

    if user_repo.find_user_by_id(session["user_id"]):
        del session["user_id"]
        return redirect("/")
    else:
        return render_template("logout.html", errors=["Nobody logged in"])


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
