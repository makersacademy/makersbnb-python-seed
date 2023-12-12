import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space

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
def get_spaces():
    connection = get_flask_database_connection(app)
    spaces_repo = SpaceRepository(connection)
    spaces_data = spaces_repo.all()
    return render_template('spaces.html', spaces_list = spaces_data)


@app.route('/single_space/<int:id>', methods=['GET'])
def get_single_space(id):
    connection = get_flask_database_connection(app)
    spaces_repo = SpaceRepository(connection)
    spaces_data = spaces_repo.find(id)
    return render_template('single_space.html', spaces_list = spaces_data)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
