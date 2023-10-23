import os
from lib.space import Space
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo_instance = SpaceRepository(connection)
    spaces = repo_instance.all()
    print(f"!!!!! REPO INSTANCE ALL = {spaces}")
    return render_template('spaces.html', spaces=spaces)



# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
