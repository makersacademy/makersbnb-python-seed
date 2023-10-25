from flask import Flask, request, render_template
from lib.user.user import User
from lib.user.user_repository import UserRepository


class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def signup(self, data):
        user = User(
            data.form.get("username"),
            data.form.get("email"),
            data.form.get("phonenumber"),
            data.form.get("password"),
        )

        if len(self.user_repository.check(user.username)) > 0:
            return "User already exists", 409
        else:
            self.user_repository.create(user)
            return user.id, 200

    def login(self, data):
        username = data.get("username")
        passwordhash = hash(data.get("password"))

        if self.user_repository.verify(username, passwordhash):
            return None

        return None
