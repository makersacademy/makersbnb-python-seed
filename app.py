import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/index', methods=['POST'])
def post_user_on_index():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = User(None, request.form['username'], request.form['user_password'], request.form['email'])
    repository.create(user)
        # below to be updated to redirect to next page
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def existing_user_log_in():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    user = User(None, request.form['username'], request.form['user_password'], request.form['email'])
    repository.create(user)
    # below to be updated to redirect to next page
    return render_template('index.html')

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
