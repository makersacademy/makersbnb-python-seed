import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# http://127.0.0.1:5001/index
# http://127.0.0.1:5001/spaces
# http://127.0.0.1:5001/spaces/new
# http://127.0.0.1:5001/requests


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# List available spaces.
@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

# List a new space as a Property owner.
@app.route('/spaces/new', methods=['GET'])
def list_new_property():
    return render_template('spaces_new.html')

# See requests that I've made and received so far.
@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
