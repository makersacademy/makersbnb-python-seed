import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from lib.user import User

app = Flask(__name__)  # Create a Flask application instance
app.secret_key = 'team_mind'  # Set a secret key for the application 

login_manager = LoginManager()  # Create a LoginManager instance
login_manager.init_app(app)  # Initialize the LoginManager with the Flask application instance

@login_manager.user_loader  # Register a user loader function with the LoginManager
def load_user(user_id):  # Define a function to load a user given a user id
    return User(user_id, users[user_id]['email'], users[user_id]['password'])  # Return a User object with the provided user id, email, and password

#LINK: http://127.0.0.1:5001/login

#-------------------------------------------------
#Our mock user database
users = {'user1': {'email': 'user1@example.com', 'password': 'password1'}, 
         'user2': {'email': 'user2@example.com', 'password': 'password2'}}
#-------------------------------------------------

#-------------------------------------------------HOME page
@app.route('/')  # Define a route for the root URL
def index():  # Define a function to handle requests to the root URL
    return render_template('home.html') 
#------------------------------------------------- HOME page



#-------------------------------------------------LOGIN page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']  # Retrieve the email from the form data
        password = request.form['password']  # Retrieve the password from the form data
        
        for user_id, user_data in users.items():  # Iterate over the users dictionary
            if user_data['email'] == email and user_data['password'] == password:
                user = User(user_id, email, password)
                login_user(user)
                return redirect(url_for('dashboard'))
        
        return 'Invalid email or password'
    
    return render_template('login.html')

#-------------------------------------------------LOGIN page




#------------------------------------------------- DASHBOARD
@app.route('/dashboard')  
@login_required  # Decorate the route to require authentication
def dashboard():  # Define a function to handle requests to the dashboard page
    return f'Hello, {current_user.id} ({current_user.email})! You are logged in.'  # Return a greeting message with the current user's id and email
#------------------------------------------------- DASHBOARD



#-------------------------------------------------------------------- LOGOUT 

@app.route('/logout')  # Define a route for logging out
@login_required  # Decorate the route to require authentication
def logout():  # Define a function to handle logout requests
    logout_user()  # Log out the user
    return 'You are logged out.'  # Return a message indicating that the user has been logged out

#-------------------------------------------------------------------- LOGOUT 



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
