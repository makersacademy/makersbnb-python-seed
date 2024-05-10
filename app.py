import os
from flask import Flask, request, render_template, url_for, redirect, session
from lib.database_connection import get_flask_database_connection
import hashlib
from lib.space_routes import apply_space_routes
# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.urandom(95)
# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db_connection = get_flask_database_connection(app)
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        db_connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db_connection = get_flask_database_connection(app)
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = db_connection.execute("SELECT FROM users WHERE username = %s AND password = %s", (username, hashed_password))

        if user:
            return redirect(url_for('get_spaces'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

from lib.space_routes import apply_space_routes
apply_space_routes(app)



from lib.booking_routes import apply_booking_routes
apply_booking_routes(app)
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))