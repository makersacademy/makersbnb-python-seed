import os
from flask import Flask, request, render_template
from lib.user_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
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

@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template("spaces.html")


@app.route('/spaces/new', methods=['GET'])
def get_spaces_new():
    return render_template("new_space.html")

@app.route('/spaces/new', methods=['POST'])
def create_space():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    name = request.form['name']
    price = request.form['price']
    description = request.form['description']
    user_id = request.form['user_id']
    #availability_from = request.form['availability_from']
    #availability_to = request.form['availability_to']
    repo.create(name, price, description, user_id)

    return render_template("spaces.html")

@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    if repo.find(name, email, password):
        return render_template("sign_up.html")
    return render_template("spaces.html")

@app.route('/login', methods=['POST'])
def validate_login():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    name = request.form['name']
    password = request.form['password']
    if repo.find(name, password):
        return render_template("spaces.html")
    return render_template("login.html")




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
