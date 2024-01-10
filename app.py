import os

from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
import jwt
import datetime
from functools import wraps
from flask import request, jsonify, make_response, session

from lib.user_repository import UserRepository
from lib.spaces_repository import SpaceRepository
from lib.spaces import Space
from lib.booking_repository import BookingRepository
from lib.booking import Booking


# Auth token generation
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Retrieve the token from the cookies
        token = request.cookies.get("token")

        # If there is no token, redirect to login with 403 Forbidden status
        if not token:
            return redirect("login"), 403

        try:
            # Decode the token to get user data
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = data["user"]
        except:
            # If token is invalid, return an error message with 403 Forbidden status
            return jsonify({"message": "Token is invalid!"}), 403

        # Pass 'current_user' as a keyword argument to avoid conflicts with
        # positional arguments from the route
        kwargs["current_user"] = current_user
        return f(*args, **kwargs)

    return decorated


# Create a new Flask app
app = Flask(__name__)

# Need work? ### NOT SECURE ###
SECRET_KEY = os.environ.get("SECRET_KEY") or "this is a secret"
app.config["SECRET_KEY"] = SECRET_KEY


def is_valid(password):
    if password is not None:
        valid_length = len(password) >= 8
        has_special_char = any(char in "!@#$%?" for char in password)
        has_digit = any(char.isdigit() for char in password)
        return valid_length and has_special_char and has_digit


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")

        if password != password_confirmation:
            return "Passwords do not match", 400

        if not is_valid(password):
            return "Invalid password", 400
            # create userRepo instance
        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)
        if user_repo.create_user(username, email, password):
            return render_template("success.html")
        else:
            return render_template("userexists.html")

    return render_template("index.html")


# success page route / html
@app.route("/success")
@token_required
def success(current_user):
    return render_template("success.html")


# login page
@app.route("/login", methods=["GET", "POST"])
def get_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)

        user = user_repo.login(username, password)
        if user is not None:
            # Token generation
            token = jwt.encode(
                {
                    "user": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                },
                app.config["SECRET_KEY"],
            )

            # Set the token in a cookie and redirect to /spaces
            response = make_response(redirect("/spaces"))
            response.set_cookie("token", token, httponly=True)
            return response

        else:
            return render_template("/login.html", error="Invalid credentials")

    return render_template("login.html")


@app.route("/logout")
def logout():
    # Create a response object for redirection
    response = make_response(redirect("/"))

    # Clear the token cookie
    response.set_cookie("token", "", expires=0)

    return response


@app.route("/spaces", methods=["GET"])
@token_required
def get_all_spaces(current_user):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.list_all_spaces()
    return render_template("/spaces/index.html", spaces=spaces)


@app.route("/spaces/new", methods=["GET"])
@token_required
def get_new_space(current_user):
    return render_template("/spaces/new.html")


@app.route("/create_space", methods=["POST"])
@token_required
def create_space(current_user):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    host = 1
    new_space = Space(
        None,
        request.form["name"],
        request.form["description"],
        float(request.form["pricePerNight"]),
        host,
    )
    repository.add_space(new_space)
    repository.add_date(
        request.form["availableFrom"], request.form["availableTo"], new_space.id
    )
    return redirect("/spaces")


@app.route("/spaces/<int:space_id>")
@token_required
def space(space_id, current_user=None):
    # 'current_user=None' is set to prevent argument conflicts.
    # Without this default value, Flask would pass 'space_id' from the URL
    # and 'current_user' from the decorator, leading to a TypeError.
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.get_space_by_id(space_id)
    dates = repository.get_available_dates(space_id)
    return render_template('/spaces/space.html', space=space, dates = dates)

@app.route('/bookings/new', methods=['POST'])
@token_required
def create_booking(current_user):
    guest_username = current_user
    space_id = request.form['space_id']
    booking_date = datetime.date.fromisoformat(request.form['date_option'])

    connection = get_flask_database_connection(app)
    guest_id = connection.execute(
        """
        SELECT id FROM users WHERE username=%s;
        """, [guest_username]
    )[0]['id']
    # space_repo = SpaceRepository(connection)
    # host_id = space_repo.get_space_by_id(space_id).host_id
    new_booking = Booking(None, booking_date, space_id, guest_id, None)
    booking_repo = BookingRepository(connection)
    booking_repo.create(new_booking)
    return redirect("/bookings/success")

@app.route('/bookings/success', methods=['GET'])
@token_required
def get_bookings_success(current_user):
    return render_template("bookings/success.html")

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
