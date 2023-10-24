import os
from flask import Flask, request, render_template, session, redirect
from lib.user_repository import UserRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)


# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create_user():
    email = request.form['email']
    password = request.form['password']
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    repository.create(email, password)
    return redirect("http://localhost:5000/account_page")

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    email = request.form['email']
    password_attempt = request.form['password_attempt']
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    if repository.check_password(email, password_attempt):
        user = repository.find_by_email(email)
        session['user_id'] = user.id
        return render_template('login_success.html')
    else:
        return render_template('login_error.html')

@app.route('/account_page')
def account_page():
    # if 'user_id' not in session:
    #     # No user id in the session so the user is not logged in.
    #     return redirect('/login')
    # else:
    #     # The user is logged in, display their account page.
    return render_template('account_page.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
