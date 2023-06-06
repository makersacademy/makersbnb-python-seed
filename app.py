import os
from flask import Flask, redirect, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /home
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/home
@app.route('/', methods=['GET'])
def get_index():
    return render_template('home.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    #connection = get_flask_database_connection(app)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    
    return redirect(f"/")
    

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
