import os, copy
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import User_repository

# Create a new Flask app
app = Flask(__name__)

# ==== Home Page - routes
#
#   current_active_user: None or username
#   index_section_id: None = see recent post
#                     active_user = see user only post
#
@app.route('/', methods=['GET'])
def index():
    return redirect('/index')

# temp route for css testing ########################
@app.route('/temp', methods=['GET'])
def temp():
    return render_template('temp.html')
####################################################

@app.route('/<home_page_section>', methods=['GET'])
def index_subsection(home_page_section):
    global active_user      #to be replaced with cookies
    _connection = get_flask_database_connection(app)
    post_repository = Post_repository(_connection)
    if home_page_section == 'current_user_posts' and active_user.is_valid():
        rows = post_repository.find(active_user.id)
    else:
        rows = post_repository.all()
    data = {
        'active_user_id': active_user.id,
        'active_user_name': active_user.name,
        'home_page_section': home_page_section,
        'post_list': rows
        }
    return render_template('index.html', data=data)




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
