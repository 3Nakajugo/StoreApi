from flask import Flask
from project.db.datab import Database
from flask_jwt_extended import (JWTManager,jwt_required, create_access_token, get_jwt_identity)


app = Flask(__name__)

from project.views import app

db = Database()
db.create_table()

if __name__ == '__main__':
    app.run(debug=True)
