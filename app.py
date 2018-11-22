from flask import Flask
from flask_jwt_extended import (JWTManager,jwt_required, create_access_token, get_jwt_identity)
from project.db.datab import Database


app = Flask(__name__)

app.config['JWT_SECRET_KEY']= "edna"
jwt = JWTManager(app)

from project.views import app

db = Database()
db.create_table()

if __name__ == '__main__':
    app.run(debug=True)
