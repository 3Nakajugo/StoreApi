from project.models import User


class UserController:
    def register_user(self, username, password, role):
        new_user = User(
            username=username,
            password=password,
            role=role
        )
