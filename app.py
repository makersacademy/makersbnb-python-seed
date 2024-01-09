import os
from flask import Flask, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.forms import RegisterForm, LoginForm
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
import hashlib

# Create a new Flask app
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "profile_page"

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    
    # Load user information
    user_repository = UserRepository(connection)
    user = user_repository.find_by_id(int(user_id))
    
    return user

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


#THIS FUNCTION HANDES THE SING IN, IF USER AND PASSWORD IS CORRECT THEN IT WILL REDIRECT TO THE PROFILE PAGE
@app.route('/sign_in', methods=['GET', 'POST'])
def get_login_details():
    form = LoginForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        user = user_repository.find_by_name(form.username.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('profile_page'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('sign_in.html', form=form)



#IF LOG IN AND PASSWORD IS CORRECT USER IS REDIRECT TO THIS PAGE. 
@app.route('/profile', methods=['GET'])
@login_required
def profile_page():
    return render_template('profile.html', user=current_user)

# I ALSO CREATED A LOG OUT FUNCTION. 
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_login_details'))


@app.route('/create_account', methods=['GET', 'POST'])
def get_create_account():
    form = RegisterForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(None, username, email, password)
        repo.create(user)

        login_user(user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('profile_page'))

    return render_template('create_account.html', form=form)

@app.route('/spaces/<int:id>', methods=['GET'])
def get_space_page(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template("space.html", space=space)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
