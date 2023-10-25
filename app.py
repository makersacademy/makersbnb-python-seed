import os
from flask import Flask, request, render_template, g, session
from lib.database_connection import get_flask_database_connection
from lib.User.user_controller import UserController
from lib.User.user_repository import UserRepository
import secrets

app = Flask(__name__)
secret = secrets.token_urlsafe(32)
app.secret_key = secret

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route("/signup", methods=["POST", "GET"])
def signup():
    user_controller = UserController(
        UserRepository(
            get_flask_database_connection(app)
        )
    )

    userid = user_controller.signup(
        request.get_json()
    )

    session['user_id'] = userid

    return userid

@app.route("/login", methods=["POST"])
def login():
    user_controller = UserController(
        UserRepository(
            get_flask_database_connection(app)
        )
    )

    userid = user_controller.login(
        request.get_json()
    )

    session['user_id'] = userid

    return userid

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5003)))
    