import os
from flask import Flask, request, render_template, g, session
from lib.database_connection import get_flask_database_connection
from lib.user.user_controller import UserController
from lib.user.user_repository import UserRepository
import secrets

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret

@app.route("/index", methods=["GET"])
def get_index():
    return render_template("index.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    user_controller = UserController(UserRepository(get_flask_database_connection(app)))

    userid = user_controller.signup(request)

    session["user_id"] = userid

    return userid


@app.route("/login")
def get_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    user_controller = UserController(UserRepository(get_flask_database_connection(app)))

    userid = user_controller.login(request)

    session["user_id"] = userid

    return userid


#  ''' this is the the frontend team's tests '''


@app.route("/spaces", methods=["GET"])
def get_spaces():
    return render_template("spaces.html")


@app.route("/spaces/new", methods=["GET"])
def get_new_space():
    return render_template("new.html")


@app.route("/requests", methods=["GET"])
def get_requests():
    return render_template("requests.html")


@app.route("/indexFrontend", methods=["POST"])
def post_index():
    email = request.form["email"]
    phone = request.form["phone"]
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]

    return "", 200


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5003)))
