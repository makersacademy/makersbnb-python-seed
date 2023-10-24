import os
from flask import Flask, request, render_template
from lib.User.user import User
from lib.User.user_repository import UserRepository as rep

class UserController:

    def __init__(self) -> None:
        pass

    def signup():
        data = request.get_json()
        user = User(
            data.get("username"),
            data.get("email"),
            data.get("phonenumber"),
            data.get("password")
        )

        if(rep.check(user.username)):
            return "user already exists"
        else:
            rep.create(user)
