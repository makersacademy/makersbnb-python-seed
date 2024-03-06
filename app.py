import os
import psycopg
from flask import Flask, request, render_template, redirect, url_for 
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
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


@app.route("/book-space", methods=["GET", "POST"])
def get_spaces():
    connection = get_flask_database_connection(app)
    # TODO get all spaces
    return render_template('book-space.html')

@app.route("/list-space", methods=["GET", "POST"])
def list_space():
    conection = get_flask_database_connection(app)
    # TODO get data from form and create new space in db
    return render_template('list-space.html')



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))




# == Your Routes Here ==
    def add_space(self, name, description, price_per_night):
        new_space = {
            'name': name,
            'description': description,
            'price_per_night': price_per_night
        }
        self.spaces.append(new_space)

    def view_spaces(self):
        return self.spaces

    def request_rental(self, space_id, date):
        # Parameters:
        #   space_id: int
        #   date: Date
        # Returns:
        #   Nothing. Creates a booking request in database for that specific date
        pass # No code here yet

    def check_status(self, booking_id):
        # Parameters:
        #   booking_id: int
        # Returns:
        #   Returns the current status of the booking
        pass # No code here yet

    def respond(self, booking_id, respond):
        # Parameters:
        #   booking_id: int
        #   response: string
        # Returns:
        #   Updates the status of booking in database based on the respond
        pass # No code here yet

