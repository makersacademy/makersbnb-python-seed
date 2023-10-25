from flask import Flask, request, render_template
from lib.User.user import User
from lib.User.user_repository import UserRepository
from hashlib import sha256

class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def signup(self, request):
        user = User(
            request.get("username"),
            request.get("email"),
            request.get("phonenumber"),
            request.get("password")
        )

        if (len(self.user_repository.check(user.username)) > 0):
            return "User already exists", 409
        else:
            self.user_repository.create(user)
            return user.id, 200

    def login(self, request):
        username = request.get("username")
        password = request.get("password") 

        hash_algorithm = sha256()
        hash_algorithm.update(password.encode("utf-8"))
        passwordhash = hash_algorithm.hexdigest()

        userReturn = self.user_repository.verify(username, passwordhash)

        if(len(userReturn) > 0):
            userRow = userReturn[0]
            user = User(
                userRow["username"],
                userRow["email"],
                userRow["phonenumber"],
                password
            )
            user.id = userRow["id"]
            return user.id, 200
        else:
            # user does not exist, return error
            return 'None'

        return None
    