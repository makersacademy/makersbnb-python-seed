import os, copy
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.space_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)




########################
# SESSION pass key
#
app.secret_key = b"_5#2LF34nxec]"
########################            


# ==== Home Page - routes
#
#   active_user: None or user_instance
#   index_section_id: .....
#
#
@app.route('/', methods=['GET'])
def index():
    return redirect('/index')

@app.route('/<home_page_section>', methods=['GET'])
def index_subsection(home_page_section):
    _connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(_connection)
    if 'id' in session:
        rows = space_repository.all()
    else:
        rows = []
    data = {
        'home_page_section': home_page_section,
        'spaces_list': rows
        }
    return render_template('index.html', data=data)



# ==== Account routes
#
#   GET arg: login
#             register
# 
@app.route('/account/<section>', methods=['GET'])
def login(section):
    if all(['email_address' not in session and
            any([
                section == 'login',
                section == 'register'
                ])
            ]):
        return render_template('account.html', login_status=section)
    elif all([
        section == 'logout',
        'email_address' in session
        ]):
        session.pop('id', None)
        session.pop('fullname', None)
        session.pop('email_address', None)
    return redirect('/')


@app.route('/user/<section>', methods=['POST'])
def user(section):
    query_result = (False, 'Generic Error')
    _connection = get_flask_database_connection(app)
    user_repository = UserRepository(_connection)
    if section == 'login':
        email_address = request.form['email_address']
        password = request.form['passcode']
        query_result = user_repository.find(email_address, password)
        #check for valid user entry
        if query_result[0]:
            session['id'] = query_result[1].id
            session['fullname'] = query_result[1].fullname
            session['email_address'] = query_result[1].email_address
            return redirect('/')
    elif section == 'register':
        name = request.form['name']
        email_address = request.form['email_address']
        password = request.form['passcode']
        query_result = user_repository.add(1, name, email_address, password)
        if query_result[0]:
            return redirect('/')
    return f"WRONG: {query_result[1]}"




# ==== Spaces routes
#
#   
# 
@app.route('/spaces/edit/<id>')
def edit_spaces(id):
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space = space_repo.find(id)
    return render_template("space_edit.html", space=space)

@app.route('/spaces', methods=['GET'])
def shows_all_spaces():
    return redirect('/')

@app.route('/spaces/update', methods=['POST'])
def update_spaces():
    id = request.form['id']
    name = request.form['name']
    desc = request.form['desc']
    price = request.form['price']

    space = Space(id, name, desc, price)
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space_repo.update(space)

    return redirect('/spaces/listings')

@app.route('/spaces/add', methods=['POST'])
def add_spaces():
    id = request.form['id']
    name = request.form['name']
    desc = request.form['desc']
    price = request.form['price']
    user_id = session['id']

    space = Space(id, name, desc, price, user_id)
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space_repo.add(space)

    return redirect('/')

@app.route('/add')
def get_add():
    if 'id' in session:
        return render_template("space_add.html")
    else:
        return "Not Authorized"

@app.route('/spaces/<id>', methods=['GET'])
def get_space(id):
    space_repo = SpaceRepository(get_flask_database_connection(app))
    space = space_repo.find(id)

    return render_template("single_space.html", space=space)

@app.route('/spaces/listings')
def spaces_listings():
    user_id = session['id']
    space_repo = SpaceRepository(get_flask_database_connection(app))
    spaces = space_repo.find(user_id, "user_id")
    print(spaces)

    return render_template("space_listings.html", spaces=spaces)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
