from lib.user_repository import UserRepository, is_valid
from lib.spaces_repository import SpaceRepository
from lib.spaces import Space
import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
import jwt
import datetime
from functools import wraps
from flask import request, jsonify, make_response, session, flash
from itertools import zip_longest

from lib.user_repository import UserRepository
from lib.spaces_repository import SpaceRepository
from lib.spaces import Space
from lib.booking_repository import BookingRepository
from lib.booking import Booking

from flask_mail import Mail, Message

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

#email config
app.config['MAIL_SERVER']="smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "MakersBnbJan2024@gmail.com"
app.config['MAIL_PASSWORD'] = "qtwi adua ptjq bygh"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

#email function
def send_email(subject, recipients, body):
    email_success = False
    msg = Message(subject)
    msg.sender ='MakersBnbJan2024@gmail.com'
    msg.sender=('MakersBnB', 'MakersBnbJan2024@gmail.com')
    msg.recipients= recipients
    msg.body = body
    try:
        mail.send(msg)
    except Exception as e:
            print(str(e))

# == Your Routes Here ==


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route("/index", methods=["GET"])
def get_index():
    return render_template("index.html")


@app.route("/bookings", methods=["GET"])
def get_bookings():
    return render_template("bookings/index.html")


@app.route("/bookings", methods=["POST"])
def goto_booking():
    space_id = request.form["id"]
    return redirect("new_booking")


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")
        print(password)
        print(password_confirmation)

        if password != password_confirmation:
            return "Passwords do not match", 400

        if not is_valid(password):
            return "Invalid password", 400

        connection = get_flask_database_connection(app)
        user_repo = UserRepository(connection)

        if user_repo.create_user(username, email, password):  # pass the plain password
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
    # Check if user is already logged in
    token = request.cookies.get("token")
    if token:
        try:
            jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            # User already logged in, redirecting to spaces page
            return redirect("/spaces")
        except jwt.ExpiredSignatureError:
            # Token is expired - user needs to log in again
            # not 'required' but catches any unforeseen errors
            flash("Your session has expired. Please log in again.", "warning")
            return redirect("/login")
        except:
            # Invalid token - continue with normal login
            return redirect("/login")

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
    response = make_response(render_template("logout.html"))

    # Clear the token cookie
    response.set_cookie("token", "", expires=0)

    return response


@app.route("/spaces", methods=["GET"])
@token_required
def get_all_spaces(current_user):
    print(current_user)
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.list_all_spaces()
    return render_template("/spaces/index.html", spaces=spaces, current_user=current_user)


@app.route("/spaces/new", methods=["GET"])
@token_required
def get_new_space(current_user):
    return render_template("/spaces/new.html")


@app.route("/create_space", methods=["POST"])
@token_required
def create_space(current_user):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    user_repo = UserRepository(connection)
    host = user_repo.username_to_id(current_user)
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
    return render_template("/spaces/space.html", space=space, dates=dates)


@app.route("/bookings/new", methods=["POST"])
@token_required
def create_booking(current_user):
    guest_username = current_user
    space_id = request.form["space_id"]
    booking_date = datetime.date.fromisoformat(request.form["date_option"])

    connection = get_flask_database_connection(app)
    guest_id = connection.execute(
        """
        SELECT id FROM users WHERE username=%s;
        """, [guest_username]
    )[0]['id']
    new_booking = Booking(None, booking_date, space_id, guest_id, None)
    booking_repo = BookingRepository(connection)
    booking_repo.create(new_booking)
    # Commented lines below may later be useful for notification sending to host
    # space_repo = SpaceRepository(connection)
    # host_id = space_repo.get_space_by_id(space_id).host_id
    # user_repo = UserRepository(connection)
    # host_username = user_repo.id_to_username(host_id)
    return redirect("/bookings/success")


@app.route("/bookings/success", methods=["GET"])
@token_required
def get_bookings_success(current_user):
    return render_template("bookings/success.html")

@app.route('/requests', methods=['GET'])
@token_required
def get_requests(current_user):
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    user_id = user_repo.username_to_id(current_user)
    # Find all bookings where user.id is the guest_id
    booking_repo = BookingRepository(connection)
    requests_made = booking_repo.find_by_guest_id(user_id)
    # Find all spaces where user.id is the host_id AND
    # find all bookings where space_id is in this list
    space_repo = SpaceRepository(connection)
    host_spaces = space_repo.get_spaces_by_host_id(user_id)
    requests_received = []
    for space in host_spaces:
        for booking in booking_repo.find_by_space_id(space.id):
            requests_received.append(booking)

    space_for_request_received = []
    for space in requests_received:
        space_for_request_received.append(space_repo.get_space_by_id(space.space_id))

    space_for_request_made = []
    for space in requests_made:
        space_for_request_made.append(space_repo.get_space_by_id(space.space_id))

    #Need to zip to access both the space info to display and the request info for routing in the html
    made_zipped_data = zip_longest(requests_made, space_for_request_made)
    received_zipped_data = zip_longest(requests_received, space_for_request_received)

    return render_template("requests/index.html",
                           requests_made=requests_made,
                           requests_received=requests_received,
                           host_spaces = host_spaces,
                           received_zipped_data=received_zipped_data,
                           made_zipped_data=made_zipped_data
                           )

@app.route('/requests/<int:booking_id>', methods=['GET'])
@token_required
def get_request_by_id(booking_id, current_user):
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking = booking_repo.find(booking_id)
    guest_id = booking.guest_id
    user_repo = UserRepository(connection)
    guest_username = user_repo.id_to_username(guest_id)
    space_id = booking.space_id
    space_repo = SpaceRepository(connection)
    space = space_repo.get_space_by_id(space_id)
    host_username = user_repo.id_to_username(space.host_id)
    current_user_id = user_repo.username_to_id(current_user)

    return render_template("bookings/booking.html",
                           current_user_id=current_user_id,
                           space=space,
                           host_username=host_username,
                           guest_username=guest_username,
                           booking=booking)

@app.route('/bookings/confirm', methods=['POST'])
@token_required
def post_confirm_booking(current_user):
    booking_id = request.form['booking_id']
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.confirm(int(booking_id))
    return redirect(f"/requests/{booking_id}")

@app.route('/bookings/reject', methods=['POST'])
@token_required
def post_reject_booking(current_user):
    booking_id = int(request.form['booking_id'])
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_repo.reject(booking_id)
    return redirect(f"/requests/{booking_id}")

@app.route('/account', methods=['GET'])
@token_required
def view_account_details(current_user):
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    user = user_repo.find_user_by_username(current_user)
    return render_template('/account.html', user=user)

@app.route('/myspaces', methods=['GET'])
@token_required
def view_user_spaces(current_user):
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)
    user_id = user_repo.username_to_id(current_user)
    space_repo = SpaceRepository(connection)
    host_spaces = space_repo.get_spaces_by_host_id(user_id)
    return render_template('/listspace.html', host_spaces=host_spaces)

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))