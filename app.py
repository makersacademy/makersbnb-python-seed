import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User


# Create a new Flask app
app = Flask(__name__)
app.secret_key = "Thisistheuserkey"
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/home', methods=['GET'])
def get_index():
    return render_template('user/home.html')






# USERS ROUTES

# SIGN UP PAGE / ROUTE

@app.route('/signup', methods = ["GET"])
def signup():
    return render_template('user/signup.html')

@app.route('/signup', methods =["POST"])
def create_new_user():
    # Connect to the database
    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    user = User(None, name, email, password)  

    if not user.is_valid():
        return render_template('user/signup.html', errors=user.generate_errors())
    user_repo.create(user)
    return redirect("/home")

@app.route("/login", methods=["GET"])
def login():
    return render_template('user/login.html')

@app.route("/login", methods=["POST"])
def login_post():
    email = request.form['email']
    password = request.form['password']

    connection = get_flask_database_connection(app)
    user_repo = UserRepository(connection)

    if user_repo.check(email, password):
        user = user_repo.find_by_email(email)
        session['user_id'] = user.id
        return redirect("/index")
    else:
        return render_template('user/login.html', error_message="Invalid email or password")
    
# logout
@app.route("/logout", methods=["GET"])
def logout():
    session.pop('user_id', None)
    return redirect("/login")







# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

