from models import User

users = [
    {
        "id": 1,
        "username": "admin",
        "password": "admin"
    },
    {
        "id": 2,
        "username": "store_attendant",
        "password": "attendant"
    }
]

username_mapping = {
    "admin": {
        "id": 1,
        "username": "admin",
        "password": "admin"
    },

    "store_attendant": {
        "id": 2,
        "username": "store_attendant",
        "password": "attendant"
    }
}

userid_mapping = {
    1: {
        "id": 1,
        "username": "admin",
        "password": "admin"
    },
    2: {
        "id": 2,
        "username": "store_attendant",
        "password": "attendant"
    }
}
# print(userid_mapping[1])


def authenticate(username, password):
    user = username_mapping.get(username)
    if user is not None and user.password == password:
        return user


def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id)
