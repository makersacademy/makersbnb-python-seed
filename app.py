import os
from flask import Flask, request, render_template, url_for, redirect
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

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
        db_connection.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        return redirect(url_for('login'))
    return render_template('register.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))