import os  # Import the os module to access environment variables
from flask import Flask, request, render_template, redirect, url_for  # Import necessary modules from Flask
from flask_login import LoginManager, login_user, login_required, logout_user, current_user  # Import modules from Flask-Login

app = Flask(__name__)  # Create a Flask application instance

# Set a secret key for the application to enable session cookies
app.secret_key = 'team_mind'

login_manager = LoginManager()  # Create a LoginManager instance
login_manager.init_app(app)  # Initialize the LoginManager with the Flask application instance

# Mock user database: Contains email addresses as keys and passwords as values
users = {
    'user1@example.com': {'password': 'password1'}, 
    'user2@example.com': {'password': 'password2'}
}

# Register a user loader function with the LoginManager
@login_manager.user_loader
def load_user(user_email):
    # Return the email address if it exists in the users dictionary, otherwise return None
    return user_email if user_email in users else None

@app.route('/')  # Define a route for the root URL
def index():  # Define a function to handle requests to the root URL
    return render_template('home.html')  # Render the home template

@app.route('/login', methods=['GET', 'POST'])  # Define a route for the login page
def login():  
    if request.method == 'POST':  # Check if the request method is POST
        email = request.form['email']  # Get the email from the form data
        password = request.form['password']  # Get the password from the form data
        
        # Check if the provided email exists in the users dictionary and if the password matches
        if email in users and users[email]['password'] == password:
            login_user(email)  # Log in the user using Flask-Login
            return redirect(url_for('dashboard'))  # Redirect to the dashboard route
        
        return 'Invalid email or password'  # Return an error message if authentication fails
    
    return render_template('login.html')  # Render the login template if the request method is GET

@app.route('/dashboard')  # Define a route for the dashboard page
@login_required  # Decorate the route to require authentication
def dashboard():  # Define a function to handle requests to the dashboard page
    return f'Hello, {current_user}! You are logged in.'  # Display a greeting message with the current user's email address

@app.route('/logout')  # Define a route for logging out
@login_required  # Decorate the route to require authentication
def logout():  # Define a function to handle logout requests
    logout_user()  # Log out the user
    return 'You are logged out.'  # Return a message indicating that the user has been logged out

if __name__ == '__main__':  # Check if the script is executed directly
    # Run the Flask application with debug mode enabled, and use the specified port or default to 5001
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
