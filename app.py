import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import *

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

@app.route('/spaces', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.list_all_spaces()
    return render_template('/spaces/index.html', spaces=spaces)

@app.route('/spaces/new', methods=['GET'])
def get_new_space():
    return render_template('/spaces/new.html')

# connection = get_flask_database_connection(app)
# repository = SpaceRepository(connection)
# spaces = repository.list_all_spaces()
# for space in spaces:
#     @app.route("/spaces/"+str(space.id),)


@app.route('/spaces/<int:space_id>')
def space(space_id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.get_space_by_id(space_id)
    return render_template('/spaces/space.html', space=space)



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 3000)))
