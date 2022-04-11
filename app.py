from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create/setup Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'pepperoni-pizza'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Instantiate LoginManager
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


import routes, models