import os
from lib.space import Space
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.available_date import AvailableDate
from lib.available_date_repository import AvailableDateRepository
import jinja_partials # to enable partials jinja html for the header for ex.

app = Flask(__name__)
jinja_partials.register_extensions(app)

# == Your Routes Here ==
@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo_instance = SpaceRepository(connection)
    spaces = repo_instance.all()
    return render_template('spaces.html', spaces=spaces)


@app.route('/spaces', methods=['POST'])
def post_spaces():
    connection = get_flask_database_connection(app)
    repo_instance = SpaceRepository(connection)

    space_name = request.form['space_name']
    description = request.form['description']
    user_id = request.form['user_id']
    price = request.form['price']

    new_space = Space(None, space_name, description,
                      price, user_id)

    repo_instance.create(new_space)
    spaces = repo_instance.all()

    return render_template('spaces.html', spaces=spaces)

@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html')


@app.route('/add_space', methods=['GET'])
def add_space():
    return render_template('add_space.html')

@app.route('/add_available_date', methods=['GET'])
def add_available_date():
    # connection = get_flask_database_connection(app)
    # repo_instance = SpaceRepository(connection)
    # spaces = repo_instance.find_all_by_user_id(id)
    #^To pass in once we get login sessions working
    return render_template('add_available_date.html')

@app.route('/add_available_date', methods=['POST'])
def post_available_date():
    connection = get_flask_database_connection(app)
    repo_instance = AvailableDateRepository(connection)

    space_id = request.form['space_id']
    date_name = request.form['date_name']

    new_available_date = AvailableDate(None, date_name, space_id)

    repo_instance.create(new_available_date)

    return render_template('add_available_date.html')

@app.route('/spaces/<id>', methods=['GET'])
def get_space_request_page(id):
    connection = get_flask_database_connection(app)
    repo_instance = SpaceRepository(connection)
    space = repo_instance.find(id)
    return render_template('request_space.html', space = space)

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))



