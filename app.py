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

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/spaces/new', methods=['GET'])
def get_new_space():
    return render_template('new.html')

@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

@app.route('/index', methods=['POST'])
def post_index():
    email = request.form['email'] 
    phone = request.form['phone']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    return '', 200

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
