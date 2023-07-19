import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.property_repository import PropertyRepository
from lib.UserRepository import UserRepository
from lib.User import User


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

@app.route('/index', methods=['POST'])
def user_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email = request.form['email']
    password = request.form['password']
    user = repository.find_by_email(email)
    if user.id == None:
        return render_template('index.html', errors = "User does not exist") , 400
    if password == user.password:
        return redirect(f"/listings")
    else:
        return render_template('index.html', errors = "Incorrect password. Please try again.") , 400

@app.route('/sign-up')
def get_sign_up():
    return render_template('sign-up.html')

@app.route('/sign-up', methods=['POST'])
def post_create_new_user():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = User(
        None,
        email = request.form['email'],
        password = request.form['password']
    )
    if user.password == "":
        return render_template('sign-up.html', error_password = True) , 400
    if user_repository.find_user_by_email(user.email) == "User already exists":
        return render_template('sign-up.html', errors = True) , 400
    else:
        user_repository.create(user)
        return redirect(f"/index")


@app.route('/listings')
def get_listings():
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return render_template('listings.html', properties=properties)

@app.route('/listings/<id>')
def get_listings_id(id):
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    property = repository.find(id)
    return render_template('listings_id.html', property=property)

@app.route('/list-property')
def get_list_property():
    return render_template('list-property.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
