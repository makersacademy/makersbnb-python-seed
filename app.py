import os
from flask import Flask, request, render_template, redirect, flash, jsonify, url_for
from lib.database_connection import get_flask_database_connection
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User

# from datetime import datetime


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /home
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/home
@app.route('/home', methods=['GET'])
def get_home():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space_list = repository.all()
    return render_template('home.html', spaces = space_list)

# open sign up page
@app.route('/signup')
def sign_up():
    return render_template("sign_up.html")

# submit sign up info
@app.route('/signup', methods = ['POST'])
def sign_up_form():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)

    # check validation
    if not has_valid_data(request.form, connection):
            return "error: inputs not valid", 400
    
    # read form data to generate new record for "users" table
    save_username = request.form.get('username')
    save_user_passwor = request.form.get('user_password')
    save_email = request.form.get('email')
    save_full_name = request.form.get('full_name')
    
    new_user = User(None, save_username, save_user_passwor, save_email, save_full_name)
    repo.add_user(new_user)

    return redirect(url_for("get_home"))

def has_valid_data(form, connection):
    handle = form['username']
    email = form['email']
    password = form['user_password']
    repo = connection.execute("SELECT * FROM users WHERE username = %s OR email = %s", [handle, email])

    if repo != []:
        return handle not in repo[0]['username'] and \
            email not in repo[0]['email'] and \
            len(password) >= 8 and \
            any(char in 'qwertyuiopasdfghjklzxcvbnm' for char in password) and \
            any(char in 'QWERTYUIOPASDFGHJKLZXCVBNM,' for char in password) and \
            any(char in '!@£$%^&*//.,' for char in password) and \
            any(char in '1234567890' for char in password)
    return len(password) >= 8 and \
        any(char in 'qwertyuiopasdfghjklzxcvbnm' for char in password) and \
        any(char in 'QWERTYUIOPASDFGHJKLZXCVBNM,' for char in password) and \
        any(char in '!@£$%^&*//.,' for char in password) and \
        any(char in '1234567890' for char in password)


@app.route("/space/<id>", methods = ["GET"])
def get_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    found_space = space_repo.find_space(id)
    return render_template("space.html", space = found_space)



# open sign up page
@app.route('/new_listing')
def new_listing():
    return render_template("new_listing.html")


# submit sign up info
@app.route('/space', methods = ['POST'])
def new_listing_form():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)

    # check validation
    # if not has_valid_data(request.form, connection):
    #         return "error: inputs not valid", 400
    
    # read form data to generate new record for "spaces" table
    save_address = request.form.get('address')
    save_description = request.form.get('description')
    save_price = request.form.get('price')
    save_user_id = 1 # from global variable / cookie

    new_space = Space(None, save_address, save_description, save_price, save_user_id)
    space_repo.add(new_space)
    new_space = space_repo.all()[-1]
    return redirect(url_for("get_space", id = f"{new_space.space_id}"))


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
