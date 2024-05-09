import os
from flask import Flask, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from lib.user import User
from lib.user_repository import *



app = Flask(__name__)  # Create a Flask application instance
app.secret_key = 'team_mind'  # Set a secret key for the application 

login_manager = LoginManager()  # Create a LoginManager instance
login_manager.init_app(app)  # Initialize the LoginManager with the Flask application instance

@login_manager.user_loader  # Register a user loader function with the LoginManager
def load_user(user_id):  # Define a function to load a user given a user id
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)
    user_data = repo.find(user_id)
    if user_data:
        return User(user_data.id, user_data.email, user_data.password)
    return None

#LINK: http://127.0.0.1:5001/login


#-------------------------------------------------LOGIN page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # Retrieve the email from the form data
        password = request.form['password']  # Retrieve the password from the form data
        connection = get_flask_database_connection(app)
        users = UserRepository(connection)
        users2 = users.all()
        for user in users2:  # Iterate over the users dictionary
            if user.email == email and user.password == password:
                user = User(user.id, email, password)
                login_user(user)
                return render_template('dashboard.html', user=user)
        
        return render_template('invalid_login.html')
    
    return render_template('login.html')

#-------------------------------------------------LOGIN page


#------------------------------------------------- DASHBOARD
@app.route('/dashboard')  
@login_required  # Decorate the route to require authentication
def dashboard():  # Define a function to handle requests to the dashboard page
    return render_template("dashboard.html")  # Return a greeting message with the current user's id and email
#------------------------------------------------- DASHBOARD


#-------------------------------------------------------------------- LOGOUT 
@app.route('/logout', methods=['POST'])  
def return_to_login():  
    return render_template('login.html') #Redirect back to login page
#-------------------------------------------------------------------- LOGOUT 


#-------------------------------------------------------------------- Incorrect password page
@app.route('/invalid_login', methods=['POST'])  
def return_to_login_after_incorrect_password():  # Define a function to handle requests to the login page after clicking return to login page
    return render_template("login.html") 
#-------------------------------------------------------------------- Incorrect password page


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
