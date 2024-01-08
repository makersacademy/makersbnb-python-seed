import os, copy
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import User_repository
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)


# ==== Home Page - routes
#
#   active_user: None or user_instance
#   index_section_id: .....
#
#
@app.route('/', methods=['GET'])
def index():
    return redirect('/index')

@app.route('/<home_page_section>', methods=['GET'])
def index_subsection(home_page_section):
    global active_user      #to be replaced with cookies
    _connection = get_flask_database_connection(app)
    #
    #
    data = {}
    return render_template('index.html', data=data)




@app.route('/spaces/edit/<id>')
def get_spaces(id):
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space = space_repo.find(id)
    
    return str(space)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
