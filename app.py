import os
from flask import Flask, request, render_template, g, session
from lib.database_connection import get_flask_database_connection
from lib.User.user_controller import UserController
from lib.User.user_repository import UserRepository
from lib.Space.space import Space
from lib.Space.space_repository import SpaceRepository
from lib.Date.Date import Date
from lib.Date.DateRepository import DateRepository
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

@app.route("/spaces/new", methods=['POST'])
def add_space():
    name = request.form['name']
    description = request.form['DescriptioN']
    owner_id = request.form['Owner_iD']
    price = request.form['price']
    date_from = request.form['date_from']
    date_to = request.form['date_to']
    
    new_space = Space(name, description, price, owner_id, date_from, date_to)
    space_repo = SpaceRepository(get_flask_database_connection(app))
    date_repo = DateRepository(get_flask_database_connection(app))

    if(space_repo.exists_already(name)):
        return 'space name exists already'
    
    space_repo.add(new_space)
    date_repo.add(new_space)

    return 'ok', 200


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
