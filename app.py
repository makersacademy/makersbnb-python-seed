import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.property_repository import PropertyRepository
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


@app.get('/properties')
def get_properties():
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return "\n".join(f"Property({property._id}, {property._property_name}, {property._user_id}, {property._description}, {property._price_per_night:.2f})" for property in properties), 200


@app.route('/add_property', methods = ['POST'])
def add_properties():
    if 'property_name' not in request.form or 'description' not in request.form or 'user_id' not in request.form or 'price_per_night' not in request.form:
        return 'One of the inputs is not filled in!', 400
    
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    property = Property(None,
                    request.form['property_name'],
                    request.form['user_id'],
                    request.form['description'],
                    request.form['price_per_night']
                    )
    repository.add(property)
    return "" , 200 

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
