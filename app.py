import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

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

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return render_template('bookings/index.html')

@app.route('/bookings', methods=['POST'])
def goto_booking():
    space_id = request.form['id']
    return redirect("new_booking")

@app.route('/bookings/new/<int:space_id>', methods=['GET'])
def new_booking(space_id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    space = space_repo.get_space_by_id(space_id)
    return render_template('bookings/new.html', space=space)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
