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
# @app.route('/index', methods=['GET'])
# def get_index():
#     return render_template('index.html')

@app.route('/spaces', methods=['GET'])
def get_space():
    return render_template('spaces.html')


@app.route('/template', methods=['GET'])
def get_template():
    return render_template('template.html')


@app.route('/addnewspace', methods=['GET'])
def get_addnewspace():
    return render_template('addnewspace.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
