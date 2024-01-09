import os
from flask import Flask, request, render_template, session
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

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

@app.route('/new_space', methods=['GET'])
def get_new_space():
    return render_template('new_space.html')

@app.route('/space', methods=['GET'])
def get_space():
    return render_template('space.html')

@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

@app.route('/request', methods=['GET'])
def get_request():
    return render_template('request.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
