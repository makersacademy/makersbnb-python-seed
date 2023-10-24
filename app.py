import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.space_parameters_validator import *

# Create a new Flask app
app = Flask(__name__)
# TO ADD - once we have access to signed user
# owner_id = current_user 

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET /new-space
# Returns the new space page with a form to add a space
# Try it:
#   ; open http://localhost:5000/new-space
@app.route('/new-space', methods=['GET'])
def get_new_space():
    return render_template('new_space.html')

# POST /
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/
@app.route('/spaces', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)

    name = request.form['name']
    description = request.form['description']
    size = request.form['size']
    price = request.form['price']

    validator = SpaceParametersValidator(name, description, size, price)
    if not validator._is_valid():
        errors = validator.generate_errors()
        return render_template('/new_space', errors=errors)

    space = Space(
        None, 
        validator.get_valid_name,
        validator.get_valid_description,
        validator.get_valid_size,
        validator.get_valid_price,
        1 #Change last number to owner_id once we have access to current user
    )

    repository.create(space)
    return redirect(f'spaces/{space.id}')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
