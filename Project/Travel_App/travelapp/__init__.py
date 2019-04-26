from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# 
# This file imports the database, user password hash, and login features from flask 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'u9bskt7z3pmr3739'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # Add route for the database to connect to
db = SQLAlchemy(app) # instance of database
bcrypt = Bcrypt(app) # instance of password hashing
login_manager = LoginManager(app) # instance of login manager
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from travelapp import routes # import the various routes to perform specific functions