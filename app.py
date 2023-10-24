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
    # Access all spaces from database table 'spaces'
    return render_template('index.html')

@app.route('/session/new')
def get_login():
    return render_template('new_session.html')

@app.route('/spaces/new')
def get_new_space():
    return render_template('new_space.html')

@app.route('/spaces/<id>')
def get_space(id):
    return render_template('space_by_id.html')

@app.route('/requests')
def get_requests():
    return render_template('all_requests.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
