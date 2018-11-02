from flask import jsonify
from project.models import User
from project.db.datab import Database


class UserController:

    def __init__(self):
        self.dbconn = Database()

    def register_user(self, username, password, role):
        new_user = User(
            username=username,
            password=password,
            role=role
        )
        self.dbconn.post_user(
            username=new_user.username, password=new_user.password, role=new_user.role)
        return jsonify({"message": "user has been created"})
