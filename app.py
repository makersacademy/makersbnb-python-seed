import os
from flask import Flask, request, render_template, redirect
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.availability_repository import AvailabilityRepository

from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    spaces = repo.all()
    return render_template("spaces.html", spaces=spaces)

@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        user = user_repository.user_details(id)
        space_repository = SpaceRepository(connection)
        spaces = space_repository.find_user_spaces(id)
        return render_template('user_homepage.html', user=user, spaces=spaces)



@app.route('/spaces/new', methods=['GET'])
def get_spaces_new():
    return render_template("new_space.html")

@app.route('/spaces/new', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    avail_repo = AvailabilityRepository(connection)
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    user_id = request.form['user_id']
    availability_from = request.form['availability_from']
    availability_to = request.form['availability_to']
    space_repo.create(name, price, description, user_id)
    space = space_repo.all()[-1]
    avail_repo.create(availability_from, availability_to, space.id)

    return redirect("/spaces")


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if not name or not email or not password:
            errors = "All fields are required."
            return render_template("sign_up.html", errors=errors)
        
        new_user = User(id=None, name=name, email=email, password=password)
        created_user = repo.create(new_user)

        if created_user:
            return redirect("/spaces", code=302)
        else:
            return render_template("sign_up.html")
        
    else:
        return render_template("sign_up.html")
        
#Commented out the below, as it's not for Minimum Viable Product. 
#AND.. I can't get it to play nice

# def check_user_exists():
#     connection = get_flask_database_connection(app)
#     repo = UserRepository(connection)
#     name = request.form['name']
#     email = request.form['email']
#     password = request.form['password']
#     if repo.find(name, email, password):
#         return render_template("sign_up.html")
#     return render_template("spaces.html")

@app.route('/login', methods=['POST'])
def validate_login():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    name = request.form['name']
    password = request.form['password']
    user_id = repo.get_user_id(name)
    if repo.find(name, password):
        return redirect("user/{}".format(user_id))
    return render_template("login.html")

@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    space_repo = SpaceRepository(connection)
    space = space_repo.find(id)
    avail_repo = AvailabilityRepository(connection)
    availabilities = avail_repo.find_space(id)
    return render_template("space_show.html", space=space, availabilities=availabilities)


@app.route('/bookings', methods=['GET'])
def get_bookings_new():
    return render_template("bookings.html")

@app.route('/bookings', methods=['GET'])
def include_dates():
    connection = get_flask_database_connection(app)
    cursor = connection.cursor()
    repo = AvailabilityRepository(connection)
    result = repo.find(1)
    return render_template('bookings.html', min_date=result.availability_from.strftime('%Y-%m-%d'), max_date=result.availability_to.strftime('%Y-%m-%d'))


# @app.route('/books', methods=['POST'])
#     def create_book():
#         # Set up the database connection and repository
#         connection = get_flask_database_connection(app)
#         repository = BookRepository(connection)

#         # Get the fields from the request form
#         title = request.form['title']
#         author_name = request.form['author_name']

#         # Create a book object
#         book = Book(None, title, author_name)

#         # Check for validity and if not valid, show the form again with errors
#         if not book.is_valid():
#             return render_template('books/new.html', book=book, errors=book.generate_errors()), 400

#         # Save the book to the database
#         book = repository.create(book)

#         # Redirect to the book's show route to the user can see it
#         return redirect(f"/books/{book.id}")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
