import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

def is_valid(password):
    if password is not None:
        valid_length = len(password)
        has_special_char = any(char in '!@#$%?' for char in password)
        has_digit = any(char.isdigit() for char in password)
        return valid_length and has_special_char and has_digit


# == Your Routes Here ==

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_confirmation = request.form.get("password_confirmation")

        if password == password_confirmation:

            # # password check function
            if not is_valid(password):
                return 'Invalid Password', 400
            # # create userRepo instance
            connection = get_flask_database_connection(app)
            user_repo = UserRepository(connection)
            user_repo.create_user(username, email, password)
            return redirect('success.html') # with button to login
        
        else: 
            return 'passwords do not match'

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')



# success page route / html


# login page




if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
