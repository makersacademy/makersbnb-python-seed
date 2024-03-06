import os
import psycopg
from flask import Flask, request, render_template, redirect, url_for 
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.space import Space
from lib.booking import Booking
from lib.user_repository import UserRepository
from lib.space_repository import SpaceRepository
from lib.booking_repository import BookingRepository
from markupsafe import escape

# Create a new Flask app
app = Flask(__name__)

# Log in logic

# pass around parameter args <?>


# == Your Routes Here ==

#== TEST EXAMPLE OF GETTING DATA FROM THE DATABASE USING CONNECTION AND REPOSITORY ==#
@app.route("/test", methods=["GET"]) # route an method/s e.g. browser send GET request to website.com/test
def get_test():
    connection = get_flask_database_connection(app) # set up connection to database on local machine
    repository = UserRepository(connection) # create a user_repo instance so we can use its methods
    users = repository.all() # use the #all method from user_repo and save in the variable 'users'
    return render_template('test.html', users=users) # return an html template and pass the template the users data
#====================================================================================#

# Sign-up form page
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    return render_template('sign-up.html')

# Sign-up POST request - create new user
@app.route("/", methods=["POST"])
def post_index():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    # get data from form when the user submits it (clicks button)
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")
    # check passwords match
    if password != confirm_password:
        return "<p>passwords do not match!</p>"
    # check username isn't already taken
    users = repository.all()
    for user in users:
        if user.user_name == email:
            return "<p>user with that email already exists!</p>"
    # if we get to here we're ok to add a new user
    user = User(
        None,
        email,
        password
    )
    repository.create(user)
    # redirect user to book a space
    return redirect(f"/book-space")

# show all spaces as a list
@app.route("/book-space", methods=["GET"])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('book-space.html', spaces=spaces)

# add a new space to the databse use a form
@app.route("/list-space", methods=["GET"])
def get_add_space_form():
    return render_template('list-space.html')

# add a new space to the databse use a form
@app.route("/list-space", methods=["POST"])
def post_add_space():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    name = request.form.get("name")
    description = request.form.get("description")
    price_per_night = request.form.get("price_per_night")
    # these aren't currently being used
    # they should probably be used to create entries in the bookings table with a loop
    available_from = request.form.get("available_from")
    available_to = request.form.get("available_to")
    # there should probably be some verification checks here...
    # make new Space object
    space = Space(
        None,
        name,
        description,
        price_per_night,
        1 # hardcoded for now
    )
    # add new space to the database
    repository.create(space)
    # redirect user to all spaces list
    return redirect(f"/book-space")

@app.route("/log-in", methods=["GET"])
def get_login():
    return render_template('log-in.html')

@app.route("/log-in", methods=["POST"])
def post_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    users = repository.all()
    username = request.form.get("email")
    password = request.form.get("password")
    # TODO implement login authentication logic (using query params?)
    for user in users:
        if user.user_name == username and user.user_password == password:
            # TODO log the user in here
            return redirect(f"/book-space")
    else:
        return "<p>no such user, please register first</p>"




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))




# == Your Routes Here ==
    # def add_space(self, name, description, price_per_night):
    #     new_space = {
    #         'name': name,
    #         'description': description,
    #         'price_per_night': price_per_night
    #     }
    #     self.spaces.append(new_space)

    # def view_spaces(self):
    #     return self.spaces

    # def request_rental(self, space_id, date):
    #     # Parameters:
    #     #   space_id: int
    #     #   date: Date
    #     # Returns:
    #     #   Nothing. Creates a booking request in database for that specific date
    #     pass # No code here yet

    # def check_status(self, booking_id):
    #     # Parameters:
    #     #   booking_id: int
    #     # Returns:
    #     #   Returns the current status of the booking
    #     pass # No code here yet

    # def respond(self, booking_id, respond):
    #     # Parameters:
    #     #   booking_id: int
    #     #   response: string
    #     # Returns:
    #     #   Updates the status of booking in database based on the respond
    #     pass # No code here yet

