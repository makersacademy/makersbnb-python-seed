from flask import Flask, request, jsonify, current_app
from flask_restful import Resource, Api
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"  # Change this to a strong, secret key
api = Api(app)
# Mock user data for demonstration purposes
users = {
    "user1": {"password": "password123"},
    "user2": {"password": "pass456"},
}


# Token generation function
def generate_token(username):
    expiration_time = datetime.utcnow() + timedelta(
        days=1
    )  # Adjust the expiration time as needed
    payload = {"username": username, "exp": expiration_time}
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token


# Token verification function
def verify_token(token):
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
        return payload["username"]
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Token is invalid


# Resource to handle user login and token generation
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if username in users and users[username]["password"] == password:
            token = generate_token(username)
            return {"token": token}, 200
        else:
            return {"message": "Invalid credentials"}, 401


# Protected resource that requires a valid token for access
class ProtectedResource(Resource):
    def get(self):
        token = request.headers.get("Authorization")
        if not token:
            return {"message": "Token is missing"}, 401
        username = verify_token(token)
        if username:
            return {"message": f"Hello, {username}! This is a protected resource."}, 200
        else:
            return {"message": "Invalid token"}, 401


api.add_resource(LoginResource, "/login")
api.add_resource(ProtectedResource, "/protected")
if __name__ == "__main__":
    app.run(debug=True)
