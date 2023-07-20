import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.property_repository import PropertyRepository
from lib.UserRepository import UserRepository
from lib.User import User
from lib.property import Property

# Create a new Flask app
app = Flask(__name__)
app.secret_key = "key"

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    session['user_id'] = None
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
        session['user_id'] = user.id 
        return redirect(f"/listings")
    else:
        return render_template('index.html', errors = "Incorrect password. Please try again.") , 400

@app.route('/sign-up')
def get_sign_up():
    session['user_id'] = None
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
    find_user = user_repository.find_by_email(user.email)
    if find_user.id != None:
        return render_template('sign-up.html', errors = True) , 400
    else:
        user_repository.create(user)
        return redirect(f"/index")

@app.route('/listings')
def get_listings():
    if session.get('user_id') == None :
        return redirect(f"/index")
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    properties = repository.all()
    return render_template('listings.html', properties=properties)

@app.route('/listings/<id>')
def get_listings_id(id):
    if session.get('user_id') == None :
        return redirect(f"/index")
    connection = get_flask_database_connection(app)
    repository = PropertyRepository(connection)
    property = repository.find(id)
    return render_template('listings_id.html', property=property)

@app.route('/list-property', methods=['GET'])
def get_list_property():
    if session.get('user_id') == None :
        return redirect(f"/index")
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    if user.id != None:
        return render_template('list-property.html')
    
@app.route('/list-property', methods=['POST'])
def post_new_property():
    current_user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    repo = PropertyRepository(connection)
    name = request.form["name"]
    description = request.form["description"]
    price = request.form["price"]
    list_of_properties = [name, description, price]
    if None in list_of_properties or "" in list_of_properties:
        return render_template('list-property.html', errors="Please fill in all the details."), 400
    else:
        property = Property(None, name, description, price, current_user_id)
        property = repo.create(property)
        return redirect(f"/listings")

@app.route('/logout')
def get_logout():
    return redirect(f"/index")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
