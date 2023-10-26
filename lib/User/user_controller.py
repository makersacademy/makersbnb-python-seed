from flask import Flask, request, render_template
from lib.user.user import User
from lib.user.user_repository import UserRepository

from hashlib import sha256


class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def signup(self, request):
        user = User(
            request.form.get("username"),
            request.form.get("email"),
            request.form.get("phonenumber"),
            request.form.get("password"),
        )

        if len(self.user_repository.check(user.username)) > 0:
            return "User already exists", 409
        else:
            self.user_repository.create(user)
            return user.id, 200

    def login(self, request):
        username = request.form.get("username")
        password = request.form.get("password")

        hash_algorithm = sha256()
        hash_algorithm.update(password.encode("utf-8"))
        passwordhash = hash_algorithm.hexdigest()

        userReturn = self.user_repository.verify(username, passwordhash)

        if len(userReturn) > 0:
            userRow = userReturn[0]
            user = User(
                userRow["username"], userRow["email"], userRow["phonenumber"], password
            )
            user.id = userRow["id"]
            return user.id
        else:
            # user does not exist, return error
            return "hello"
