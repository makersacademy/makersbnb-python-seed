import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
properties_name = [
    {"name": "Amazing sea views", "location": "Canary Islands", "price": "£400 a night", "description": "Minutes from the beach, perfect for early morning walks and watching the besutiful sunset in the evenings."},
    {"name": "Location, Location, Location...", "location": "London", "price": "£1000 a night", "description": "close to central London and its ameneties"},
    {"name": "Earthen home", "location": "Terrasini, Italy", "price": "$1,000,000", "description": "A sophisticated chest, cozy, immersed in nature and unmistakable style."}
]

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html', properties=properties_name)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
