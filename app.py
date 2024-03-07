import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.property import Property

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# Placeholder for property booking
@app.route('/properties/<int:id>', methods=['GET'])
def show_property_by_id(id):
    property = Property(1, "Burnaston Road", 1, "hot", 20.50)
    return render_template('get_property.html', property=property)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
