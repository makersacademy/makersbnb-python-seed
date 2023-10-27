import os
from flask import Flask, request, render_template, g, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.user.user_controller import UserController
from lib.user.user_repository import UserRepository
from lib.space.space_controller import SpaceController
from lib.space.space_repository import SpaceRepository
from lib.date.DateRepository import DateRepository
from lib.space.space import Space
import secrets

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret


@app.route("/", methods=["GET"])
def get_index():
    return render_template("index.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    user_controller = UserController(UserRepository(get_flask_database_connection(app)))

    userid = user_controller.signup(request)

    session["user_id"] = userid

    return redirect("/spaces")


@app.route("/logout")
def get_logout():
    session["user_id"] = False
    return redirect("/")


@app.route("/login")
def get_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    user_controller = UserController(UserRepository(get_flask_database_connection(app)))

    userid = user_controller.login(request)
    print(userid)
    session["user_id"] = userid
    return redirect("/spaces")


@app.route("/spaces/new", methods=["POST"])
def add_space():
    name = request.form["name"]
    description = request.form["description"]

    start_date = request.form["date_from"]
    end_date = request.form["date_to"]
    new_space = Space(name, description, session["user_id"], start_date, end_date)
    space_repo = SpaceRepository(get_flask_database_connection(app))
    date_repo = DateRepository(get_flask_database_connection(app))

    if space_repo.exists_already(name):
        return "space name exists already"

    space_repo.add(new_space)
    date_repo.add(new_space)

    return redirect('/spaces')


#  ''' this is the the frontend team's tests '''


@app.route("/spaces", methods=["GET"])
def get_spaces():
    space_controller = SpaceController(
        SpaceRepository(get_flask_database_connection(app)),
        DateRepository(get_flask_database_connection(app)),
    )
    spaces = space_controller.list_all()
    return render_template("spaces.html", spaces=spaces)


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
