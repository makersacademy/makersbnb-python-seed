import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

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

# @app.route('/test', methods=['GET'])
# def get_test():
#     return render_template('test.html')

@app.route('/testsubmit', methods=["POST"])
def submit_signup():
    connection = get_flask_database_connection(app)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return render_template('test.html', name=name, email=email, password=password)
# The above function gathers all of the details for sign up

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/testlogin', methods=["POST"])
def submit_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    return render_template('test_loggedin.html', email=email, password=password)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

