import os
from lib.space import Space
from flask import Flask, redirect, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.user import User
from lib.available_date import AvailableDate
from lib.available_date_repository import AvailableDateRepository
import jinja_partials # to enable partials jinja html for the header for ex.

# == admin stuff ==

app = Flask(__name__)
jinja_partials.register_extensions(app)


# == Your Routes Here ==

## Home

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html.jinja')

## Spaces

@app.route('/spaces/index', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo_instance = SpaceRepository(connection)
    spaces = repo_instance.all()
    return render_template('/spaces/index.html.jinja', spaces=spaces)

@app.route('/spaces/add_a_space_form', methods=['GET'])
def get_space_form():
    return render_template('/spaces/add_a_space_form.html.jinja')

### create a space post method
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

    return render_template('spaces/index.html.jinja', spaces=spaces)

def get_space_form():
    return render_template('/spaces/add_a_space_form.html.jinja')
## Signup
@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html.jinja')


@app.route('/sign_up', methods=['POST'])
def post_username_sign_up():
    connection = get_flask_database_connection(app)
    repo_instance = UserRepository(connection)
    print(request.form,"!!!!!!!!!!!!!!!")
    username = request.form['username']
    
    new_user = User(username, "", None)
    repo_instance.create(new_user)
    user = repo_instance.find_by_username(username)
    return redirect(f'profile_page/{user.id}')




@app.route('/add_available_date', methods=['GET'])
def add_available_date():
    # connection = get_flask_database_connection(app)
    # repo_instance = SpaceRepository(connection)
    # spaces = repo_instance.find_all_by_user_id(id)
    #^To pass in once we get login sessions working
    return render_template('add_available_date.html.jinja')

@app.route('/add_available_date', methods=['POST'])
def post_available_date():
    connection = get_flask_database_connection(app)
    repo_instance = AvailableDateRepository(connection)

    space_id = request.form['space_id']
    date_name = request.form['date_name']

    new_available_date = AvailableDate(None, date_name, space_id)

    repo_instance.create(new_available_date)

    return render_template('/spaces/add_available_date.html.jinja')

@app.route('/spaces/<id>', methods=['GET'])
def get_space_request_page(id):
    connection = get_flask_database_connection(app)
    repo_instance = SpaceRepository(connection)
    space = repo_instance.find(id)
    return render_template('spaces/request_space.html.jinja', space = space)

@app.route('/profile_page/<id>', methods=['GET'])
def profile_page(id):
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    users = repo.all()
    print(users)
    user = repo.find(str(id))
    return render_template('profile_page.html.jinja', user=user)

# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

@app.route('/', methods=['GET'])
def get_app_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
    



