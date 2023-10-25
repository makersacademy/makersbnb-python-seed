from flask import Flask, request, render_template
from lib.User.user import User
from lib.User.user_repository import UserRepository

class UserController:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def signup(self, data):
        user = User(
            data.get("username"),
            data.get("email"),
            data.get("phonenumber"),
            data.get("password")
        )

        if (len(self.user_repository.check(user.username)) > 0):
            return "User already exists", 409
        else:
            self.user_repository.create(user)
            return user.id, 200

    def login(self, data):
        username = data.get("username")
        passwordhash = hash(data.get("password"))

        if(self.user_repository.verify(username, passwordhash)):
            return None

        return None
    
  