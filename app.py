import os
from flask import Flask, request, render_template, session, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User, UserRepo
# Create a new Flask app
app = Flask(__name__)
app.secret_key='12'
# == Your Routes Here ==
  
# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def signup():
    username = request.form['username'].strip()
    email = request.form['email'].strip()
    password = request.form['password']
    new_user = User(None, username, email, password, None)
    connection = get_flask_database_connection(app)
    user_repo = UserRepo(connection)
    errors = user_repo.check_user(new_user)
    if errors:
        print(errors)
        return redirect('/')
    else:
        # Save the user to the database and then go back to index page
        user_id = user_repo.create_user(new_user) 
        session['user_id'] = user_id
        return render_template('spaces.html')
    
    
    
    
    


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
