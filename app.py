import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
import jwt
import datetime
from functools import wraps
from flask import request, jsonify, make_response, session


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("token")  # Get token from cookies

        if not token:
            return redirect("login"), 403

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = data["user"]
        except:
            return jsonify({"message": "Token is invalid!"}), 403

        return f(current_user, *args, **kwargs)

    return decorated


# Create a new Flask app
app = Flask(__name__)

# Need work?
SECRET_KEY = os.environ.get("SECRET_KEY") or "this is a secret"
print(SECRET_KEY)
app.config["SECRET_KEY"] = SECRET_KEY


def is_valid(password):
    if password is not None:
        valid_length = len(password) >= 8
        has_special_char = any(char in "!@#$%?" for char in password)
        has_digit = any(char.isdigit() for char in password)
        return valid_length and has_special_char and has_digit


# == Your Routes Here ==


@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")

        if password == password_confirmation:
            # # password check function
            if not is_valid(password):
                return "Invalid Password", 400  # TODO - html page?
            # # create userRepo instance
            connection = get_flask_database_connection(app)
            user_repo = UserRepository(connection)
            user_repo.create_user(username, email, password)
            return redirect("success")  # with button to login

        else:
            return "passwords do not match"

    return render_template("index.html")


# success page route / html
@app.route("/success")
@token_required
def success():
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


# placeholder - remove on merge
@app.route("/spaces")
@token_required
def protected_route(current_user):
    return render_template("spaces.html")


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
