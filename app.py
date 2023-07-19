import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.User import User
from lib.UserRepository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/sign-up')
def get_sign_up():
    return render_template('sign-up.html')

@app.route('/sign-up', methods=['POST'])
def post_create_new_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = User(
        None,
        email = request.form['email'],
        password = request.form['password']
    )
    if user.password == "":
        return render_template('sign-up.html', error_password = True) , 400
    if user_repository.find_user_by_email(user.email) == "User already exists":
        return render_template('sign-up.html', errors = True) , 400
    else:
        user_repository.create(user)
        return redirect(f"/index")


@app.route('/listings')
def get_listings():
    return render_template('listings.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
